from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from ..forms import PlaylistForm
from app.models import db, playlist_songs, Playlist, Song, Album, User
from .AWS_helpers import upload_file_to_s3, get_unique_filename, remove_file_from_s3

playlist_routes = Blueprint('playlists', __name__)

@playlist_routes.route('/current')
@login_required
def get_users_playlists():
    """
    Gets all of the current user's playlists
    """
    playlists = Playlist.query.filter(Playlist.owner_id == current_user.id).all()

    user_playlists = []

    for playlist in playlists:
        user_playlists.append(playlist.to_dict())

    return { 'playlists': user_playlists }

@playlist_routes.route('/<int:id>')
@login_required
def get_single_playlist(id):
    """
    Gets all the info about a playlist
    """
    playlist = Playlist.query.get(id)

    if playlist is None:
        return { 'errors': 'Playlist not found' }, 404
    
    if playlist.owner_id != current_user.id:
        return { 'errors': 'Unauthorized' }, 401
    
    return { 'playlist': playlist.to_dict() }

@playlist_routes.route('/<int:id>/songs')
@login_required
def get_songs_in_playlist(id):
    """
    Gets all of the songs in a playlist
    """
    playlist = Playlist.query.get(id)
    user = User.query.get(current_user.id)

    if playlist is None:
        return { 'errors': 'Playlist not found' }, 404

    if playlist.owner_id != current_user.id:
        return { 'errors': 'Unauthorized' }, 401

    song_list = []

    for song in playlist.songs:
        # album = Album.query.get(song.album_id)
        album = db.session.query(Album, User) \
        .join(User, song.created_by == User.id) \
        .filter(Album.id == song.album_id).first()
        liked = False
        if song in user.liked_songs:
            liked = True

        song_list.append( { **song.to_dict(), 'liked': liked, 'album': { **album[0].to_dict(), 'created_by': {**album[1].private_to_dict()} } })

    return { 'songs': song_list }

@playlist_routes.route('/<int:playlistId>/song/<int:songId>', methods=['POST'])
@login_required
def add_song_to_playlist(playlistId, songId):
    """
    Adds a song to a playlist
    """
    playlist = Playlist.query.get(playlistId)
    song = Song.query.get(songId)

    if playlist is None:
        return { 'errors': 'Playlist not found' }, 404
    
    if Song is None:
        return { 'errors': 'Song not found' }, 404

    if playlist.owner_id != current_user.id:
        return { 'errors': 'Unauthorized' }, 401
    
    if song in playlist.songs:
        return { 'errors': 'Song is already in playlist' }, 500

    playlist.songs.append(song)
    db.session.commit()

    song_list = []

    for song in playlist.songs:
        album = db.session.query(Album, User) \
        .join(User, song.created_by == User.id) \
        .filter(Album.id == song.album_id).first()

        song_list.append( { **song.to_dict(), 'album': { **album[0].to_dict(), 'created_by': {**album[1].private_to_dict()} } })

    return { 'songs': song_list }

@playlist_routes.route('/<int:playlistId>/song/<int:songId>', methods=['DELETE'])
@login_required
def remove_song_from_playlist(playlistId, songId):
    """
    Removes a song from a playlist
    """
    playlist = Playlist.query.get(playlistId)
    song = Song.query.get(songId)

    if playlist is None:
        return { 'errors': 'Playlist not found' }, 404
    
    if song is None:
        return { 'errors': 'Song not found' }, 404

    if playlist.owner_id != current_user.id:
        return { 'errors': 'Unauthorized' }, 401

    for currentSong in playlist.songs:
        if currentSong.id == songId:
            playlist.songs.remove(currentSong)
            db.session.commit()
            return { 'message': 'Successfully deleted' }, 200
        
    return { 'errors': 'Song not in playlist' }, 404


@playlist_routes.route('/new/<int:count>', methods=['POST'])
@login_required
def create_new_playlist(count):
    """
    Creates a new playlist
    """
    user = User.query.get(current_user.id)

    new_playlist = Playlist(
        name=f"My Playlist #{count}",
        owner_id=user.id
    )

    db.session.add(new_playlist)
    db.session.commit()
    
    return { 'playlist': new_playlist.to_dict() }

@playlist_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_playlist(id):
    """
    Deletes a playlist by ID
    """
    playlist = Playlist.query.get(id)

    if playlist is None:
        return { 'errors': 'Resource not found'}, 404

    if playlist.owner_id != current_user.id:
        return { 'errors' 'Unauthorized' }, 401
    
    db.session.delete(playlist)
    db.session.commit()

    return { 'message': 'Successfully deleted' }, 200

@playlist_routes.route('/<int:id>', methods=['PUT'])
@login_required
def update_playlist(id):
    """
    Update playlist by id
    """
    playlist = Playlist.query.get(id)

    if playlist is None:
        return { 'errors': 'Resource not found'}, 404
    
    if playlist.owner_id != current_user.id:
        return { 'errors' 'Unauthorized' }, 401
    
    form = PlaylistForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        
        if form.data['picture']:
            remove_file_from_s3(playlist.picture)

            image = form.data["picture"]
            image.filename = get_unique_filename(image.filename)
            upload = upload_file_to_s3(image)
            # print(upload)
            if "url" not in upload:
                # if the dictionary doesn't have a url key
                # it means that there was an error when you tried to upload
                # so you send back that error message (and you printed it above)
                return { 'errors': 'URL not in upload' }, 400
        
            url = upload['url']
            playlist.name = form.data['name']
            playlist.picture = url
            db.session.commit()
            return { **playlist.to_dict() }
        else:
            playlist.name = form.data['name']
            db.session.commit()
            return { **playlist.to_dict() }
        
    if form.errors:
        return { 'errors': form.errors }

@playlist_routes.route('/likedSongs')
@login_required
def get_users_liked_songs():
    """
    Gets current user's liked songs
    """
    user = User.query.get(current_user.id)

    song_list = []

    for song in user.liked_songs:
        album = db.session.query(Album, User) \
        .join(User, song.created_by == User.id) \
        .filter(Album.id == song.album_id).first()
        liked = False
        if song in user.liked_songs:
            liked = True

        song_list.append( { **song.to_dict(), 'liked': liked, 'album': { **album[0].to_dict(), 'created_by': {**album[1].private_to_dict()} } })

    return { 'songs': song_list }

@playlist_routes.route('/likedSongs/<int:songId>', methods=['POST'])
@login_required
def add_song_to_liked_songs(songId):
    """
    Add song to liked songs
    """
    user = User.query.get(current_user.id)
    song = Song.query.get(songId)

    if song is None:
        return { 'errors': 'Song not found' }, 404

    if song in user.liked_songs:
        return { 'errors': 'Song already in Liked Songs' }, 500

    user.liked_songs.append(song)
    db.session.commit()

    song_list = []

    for song in user.liked_songs:
        song_list.append({ **song.to_dict() })

    return { 'songs': song_list }

@playlist_routes.route('/likedSongs/<int:songId>', methods=['DELETE'])
@login_required
def remove_song_from_liked_songs(songId):
    """
    Removes a song from liked songs
    """
    user = User.query.get(current_user.id)
    song = Song.query.get(songId)

    if song is None:
        return { 'errors': 'Song not found' }, 404

    if song not in user.liked_songs:
        return { 'errors': 'Song not in Liked Songs' }
    
    user.liked_songs.remove(song)
    db.session.commit()

    return { 'message': 'Successfully removed' }