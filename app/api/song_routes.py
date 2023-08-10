from flask import Blueprint, request
from flask_login import login_required
from app.models import db, Album, User, Song

song_routes = Blueprint('songs', __name__)

@song_routes.route('/<int:id>')
def get_songs_for_album(id):
    all_songs = Song.query.filter(Song.album_id == id).all()

    songs = []

    for song in all_songs:
        songs.append(song.to_dict())
    
    return songs
