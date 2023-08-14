from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from ..forms import AlbumForm, UpdateAlbumForm
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

    if playlist is None:
        return { 'errors': 'Playlist not found' }, 404

    if playlist.owner_id != current_user.id:
        return { 'errors': 'Unauthorized' }, 401

    songs = [song for song in playlist.songs]

    song_list = []

    for song in songs:
        # album = Album.query.get(song.album_id)
        album = db.session.query(Album, User) \
        .join(User, song.created_by == User.id) \
        .filter(Album.id == song.album_id).first()

        song_list.append( { **song.to_dict(), 'album': { **album[0].to_dict(), 'created_by': {**album[1].private_to_dict()} } })

    return { 'songs': song_list }

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
        return { 'error': 'Resource not found'}, 404

    if playlist.owner_id != current_user.id:
        return { 'errors' 'Unauthorized' }, 401
    
    db.session.delete(playlist)
    db.session.commit()

    return { 'message': 'Successfully deleted' }, 200