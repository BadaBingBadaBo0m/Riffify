from app.models import db, Song, environment, SCHEMA
from sqlalchemy import text

def seed_songs():
    never_there = Song(
        name='Never There',
        created_by=1,
        album_id=1,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Currents-never-there.mp3'
    )
    a_flag_to_wave = Song(
        name='A Flag To Wave',
        created_by=1,
        album_id=1,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Currents-a-flag-to-wave.mp3'
    )
    poverty_of_self = Song(
        name='Poverty of Self',
        created_by=1,
        album_id=1,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Currents-poverty-of-self.mp3'
    )
    monsters = Song(
        name='Monsters',
        created_by=1,
        album_id=1,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Currents-Monsters.mp3'
    )
    kill_the_ache = Song(
        name='Kill The Ache',
        created_by=1,
        album_id=1,
        song_body='/Currents-Kill-The-Ache.mp3'
    )
    Let_me_leave = Song(
        name='Let Me Leave',
        created_by=1,
        album_id=1,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Currents-let-me-leave.mp3'
    )
    origin = Song(
        name='origin',
        created_by=1,
        album_id=1,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Currents-origin.mp3'
    )
    split = Song(
        name='Split',
        created_by=1,
        album_id=1,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Currents-split.mp3'
    )
    second_skin = Song(
        name='Second Skin',
        created_by=1,
        album_id=1,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Currents-second-skin.mp3'
    )
    how_i_fall_apart = Song(
        name='How I Fall Apart',
        created_by=1,
        album_id=1,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Currents-how-I-fall-apart.mp3'
    )
    better_days = Song(
        name='Better Days',
        created_by=1,
        album_id=1,
        song_body='/Currents-Better-days.mp3'
    )

    db.session.add(never_there)
    db.session.add(a_flag_to_wave)
    db.session.add(poverty_of_self)
    db.session.add(monsters)
    db.session.add(kill_the_ache)
    db.session.add(Let_me_leave)
    db.session.add(origin)
    db.session.add(split)
    db.session.add(second_skin)
    db.session.add(how_i_fall_apart)
    db.session.add(better_days)
    db.session.commit()

def undo_songs():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM songs"))
        
    db.session.commit()