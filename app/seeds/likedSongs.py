from app.models import db, LikedSong, environment, SCHEMA
from sqlalchemy import text

def seed_liked_songs():
    the_way_it_ends = LikedSong(
        user_id=1,
        song_id=1
    )

    db.session.add(the_way_it_ends)
    db.session.commit()

def undo_liked_songs():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM liked_songs"))
        
    db.session.commit()