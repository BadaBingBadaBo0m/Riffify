from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime
from .playlist_songs import playlist_songs

class Playlist(db.Model):
    __tablename__ = 'playlists'

    if environment == 'production':
        __table_args__ = { 'schema': SCHEMA }

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')))
    description = db.Column(db.String(1000))
    picture = db.Column(db.String, default='/playlist-pic.png')
    song_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('songs.id')))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)

    owner = db.relationship('User', back_populates='playlists')
    songs = db.relationship('Song', secondary=playlist_songs, back_populates='playlists')

    def to_dict(self):
        return {
            'id': self.id,
            'owner_id': self.owner_id,
            'name': self.name,
            'description': self.description,
            'picture': self.picture,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }