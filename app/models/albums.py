from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Album(db.Model):
    __tablename__ = 'albums'

    if environment == 'production':
        __table_args__ = { 'schema': SCHEMA }

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    artists = db.Column(db.String)
    created_by_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')))
    description = db.Column(db.String(1000), nullable=False)
    art = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)
    
    songs = db.relationship('Song', back_populates='albums', cascade='all, delete-orphan')
    created_by_user = db.relationship('User', back_populates='albums')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'artists': self.artists,
            'created_by_id': self.created_by_id,
            'description': self.description,
            'art': self.art,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }