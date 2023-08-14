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
    the_death_we_seek = Song(
        name='The Death We Seek',
        created_by=1,
        album_id=2,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/The+Death+We+Seek.mp3'
    )
    living_in_tragedy = Song(
        name='Living In Tragedy',
        created_by=1,
        album_id=2,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Living+In+Tragedy.mp3'
    )
    unfamiliar = Song(
        name='Unfamiliar',
        created_by=1,
        album_id=2,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Unfamiliar.mp3'
    )
    so_alone = Song(
        name='So Alone',
        created_by=1,
        album_id=2,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/So+Alone.mp3'
    )
    over_and_over = Song(
        name='Over And Over',
        created_by=1,
        album_id=2,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Over+And+Over.mp3'
    )
    beyond_this_road = Song(
        name='Beyond This Road',
        created_by=1,
        album_id=2,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Beyond+This+Road.mp3'
    )
    vengeance = Song(
        name='Vengeance',
        created_by=1,
        album_id=2,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Vengeance.mp3'
    )
    gone_astray = Song(
        name='Gone Astray',
        created_by=1,
        album_id=2,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Gone+Astray.mp3'
    )
    remember_me = Song(
        name='Remember Me',
        created_by=1,
        album_id=2,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Remember+Me.mp3'
    )
    guide_us_home = Song(
        name='Guide Us Home',
        created_by=1,
        album_id=2,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Guide+Us+Home.mp3'
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
    db.session.add(the_death_we_seek)
    db.session.add(living_in_tragedy)
    db.session.add(unfamiliar)
    db.session.add(so_alone)
    db.session.add(over_and_over)
    db.session.add(beyond_this_road)
    db.session.add(vengeance)
    db.session.add(gone_astray)
    db.session.add(remember_me)
    db.session.add(guide_us_home)
    db.session.commit()

def undo_songs():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM songs"))
        
    db.session.commit()