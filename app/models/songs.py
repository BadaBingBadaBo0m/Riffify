from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime
from .playlist_songs import playlist_songs

class Song(db.Model):
    __tablename__ = 'songs'

    if environment == 'production':
        __table_args__ = { 'schema': SCHEMA }

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    artists = db.Column(db.String(50))
    created_by = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')))
    plays = db.Column(db.Integer, default=0)
    song_body = db.Column(db.String)
    song_length = db.Column(db.Integer)
    album_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('albums.id')))
    # playlist_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('playlists.id')))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)

    albums = db.relationship('Album', back_populates='songs')
    playlists = db.relationship('Playlist', secondary=playlist_songs, back_populates='songs')
    liked_songs = db.relationship('LikedSong', back_populates='songs', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'artists': self.artists,
            'created_by': self.created_by,
            'plays': self.plays,
            'song_length': self.song_length,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }