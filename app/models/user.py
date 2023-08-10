from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    profile_pic = db.Column(db.String, default='/userpic.png')
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)
    hashed_password = db.Column(db.String(255), nullable=False)

    playlists = db.relationship('Playlist', back_populates='owner', cascade='all, delete-orphan')
    albums = db.relationship('Album', back_populates='created_by_user', cascade='all, delete-orphan')
    liked_songs = db.relationship('LikedSong', back_populates='user', cascade='all, delete-orphan')

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'profile_pic': self.profile_pic,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def private_to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'profile_pic': self.profile_pic
        }