from app.models import db, playlist_songs, environment, SCHEMA
from sqlalchemy import text

def seed_playlist_songs():
    connection = db.engine.connect()

    data = [
        {"playlist_id":1, "song_id": 1}
    ]

    for song in data:
        connection.execute(playlist_songs.insert(), song)

    connection.close()

def undo_playlist_songs():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM liked_songs"))
        
    db.session.commit()