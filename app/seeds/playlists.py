from app.models import db, Playlist, environment, SCHEMA
from sqlalchemy import text

def seed_playlists():
    bangers = Playlist(
        name='Bangers',
        owner_id=1
    )
    sorta_bangers = Playlist(
        name='Sorta-bangers',
        owner_id=1
    )
    i_am_out_of_name_ideas = Playlist(
        name='I am out of name ideas',
        owner_id=2
    )

    db.session.add(bangers)
    db.session.add(sorta_bangers)
    db.session.add(i_am_out_of_name_ideas)
    db.session.commit()

def undo_playlists():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM playlists"))
        
    db.session.commit()