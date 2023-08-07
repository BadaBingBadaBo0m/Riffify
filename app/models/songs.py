from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Song(db.Model):
    __tablename__ = 'songs'

    if environment == 'production':
        __table_args__ = { 'schema': SCHEMA }

    id = db.Column(id.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    artists = db.Column(db.String(50))
    created_by = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')))
    plays = db.Column(db.Integer, default=0)
    song_length = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)

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