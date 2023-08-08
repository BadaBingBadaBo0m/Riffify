from app.models import db, Playlist, environment, SCHEMA
from sqlalchemy import text

def seed_playlists():
    better_days = Playlist(
        name='Bangers',
        owner_id=1
    )

    db.session.add(better_days)
    db.session.commit()

def undo_playlists():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM playlists"))
        
    db.session.commit()