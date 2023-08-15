from app.models import db, liked_songs, environment, SCHEMA
from sqlalchemy import text

def seed_liked_songs():
    connection = db.engine.connect()

    data = [
        {"user_id":1, "song_id": 1},
        {"user_id":1, "song_id": 2},
        {"user_id":1, "song_id": 3},
    ]

    for song in data:
        connection.execute(liked_songs.insert(), song)

    connection.close()


    # user1Song1 = LikedSong(
    #     user_id=1,
    #     song_id=1
    # )
    # user1Song2 = LikedSong(
    #     user_id=1,
    #     song_id=2
    # )
    # user1Song3 = LikedSong(
    #     user_id=1,
    #     song_id=3
    # )
    # user1Song4 = LikedSong(
    #     user_id=1,
    #     song_id=4
    # )
    # user1Song5 = LikedSong(
    #     user_id=1,
    #     song_id=15
    # )


    # db.session.add(user1Song1)
    # db.session.add(user1Song2)
    # db.session.add(user1Song3)
    # db.session.add(user1Song4)
    # db.session.add(user1Song5)
    # db.session.commit()

def undo_liked_songs():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM liked_songs"))
        
    db.session.commit()