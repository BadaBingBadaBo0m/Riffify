from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class LikedSong(db.Model):
    __tablename__ = 'liked_songs'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')))
    song_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('songs.id')))
    # songs = db.relationship('Song', back_populates='liked_songs', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'song_id': self.song_id
        }