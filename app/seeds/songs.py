from app.models import db, Song, environment, SCHEMA
from sqlalchemy import text

def seed_songs():
    better_days = Song(
        name='Better Days',
        created_by=1,
        album_id=1,
        playlist_id=1
    )

    db.session.add(better_days)
    db.session.commit()

def undo_songs():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM songs"))
        
    db.session.commit()