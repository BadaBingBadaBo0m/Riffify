from .db import db, environment, SCHEMA, add_prefix_for_prod

playlist_songs = db.Table(
    'playlist_songs',
    db.Model.metadata,
    db.Column('id', db.Integer, primary_key=True, autoincrement=True),
    db.Column('playlist_id', db.Integer, db.ForeignKey(add_prefix_for_prod('playlists.id'))),
    db.Column('song_id', db.Integer, db.ForeignKey(add_prefix_for_prod('songs.id')))
)

if environment == "production":
    playlist_songs.schema = SCHEMA
