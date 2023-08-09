from app.models import db, Album, environment, SCHEMA
from sqlalchemy import text

def seed_albums():
    the_way_it_ends = Album(
        name='The Way It Ends',
        created_by_id=1
    )
    aggressive = Album(
        name='Aggressive',
        created_by_id=1
    )
    dissentient = Album(
        name='dissentient',
        created_by_id=2
    )
    the_death_of_peace_of_mind = Album(
        name='THE DEATH OF PEACE OF MIND',
        created_by_id=2
    )

    db.session.add(the_way_it_ends)
    db.session.add(aggressive)
    db.session.add(dissentient)
    db.session.add(the_death_of_peace_of_mind)
    db.session.commit()

def undo_albums():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM albums"))
        
    db.session.commit()