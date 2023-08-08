from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Album(db.Model):
    __tablename__ = 'albums'

    if environment == 'production':
        __table_args__ = { 'schema': SCHEMA }

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    artists = db.Column(db.String)
    created_by = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')))
    description = db.Column(db.String(1000))
    art = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)
    
    songs = db.relationship('Song', back_populates='albums', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'artists': self.artists,
            'created_by': self.created_by,
            'description': self.description,
            'art': self.art,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }