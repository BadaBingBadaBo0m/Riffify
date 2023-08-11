from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import db, Album, User, Song
from ..forms import SongForm
from .AWS_helpers import upload_file_to_s3, get_unique_filename, remove_file_from_s3

song_routes = Blueprint('songs', __name__)

@song_routes.route('/<int:id>')
def get_songs_for_album(id):
    all_songs = Song.query.filter(Song.album_id == id).all()

    songs = []

    for song in all_songs:
        songs.append(song.to_dict())
    
    return songs

@song_routes.route('/new/<int:albumId>', methods=['POST'])
@login_required
def create_new_song(albumId):
    """
    Create a song for an album
    """
    user = User.query.get(current_user.id)
    album = Album.query.get(albumId)
    form = SongForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if (album.created_by_id != user.id):
        return { 'errors': 'Unauthorized' }

    if form.validate_on_submit():
        song = form.data["song_body"]
        song.filename = get_unique_filename(song.filename)
        upload = upload_file_to_s3(song)
        # print(upload)

        if "url" not in upload:
        # if the dictionary doesn't have a url key
        # it means that there was an error when you tried to upload
        # so you send back that error message (and you printed it above)
            return { 'errors': 'URL not in upload' }

        url = upload["url"]
        new_song = Song(
            name=form.data['name'],
            created_by=current_user.id,
            song_body=url,
            album_id=albumId
        )

        db.session.add(new_song)
        db.session.commit()

        return { 'song': new_song.to_dict() }, 200

    if form.errors:
        print(form.errors)
        return { 'errors': form.errors }
    
@song_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_song(id):
    """
    Delete a song
    """
    song = Song.query.get(id)

    if song is None:
        return { 'error': 'Song not found' }, 404
    
    if current_user.id != song.created_by:
        return { 'errors': 'Unauthorized' }
    
    remove_file_from_s3(song.song_body)
    db.session.delete(song)
    db.session.commit()
    return { 'message': 'Successfully deleted' }, 200