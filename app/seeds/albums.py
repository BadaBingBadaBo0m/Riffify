from app.models import db, Album, environment, SCHEMA
from sqlalchemy import text

def seed_albums():
    the_way_it_ends = Album(
        name='The Way It Ends',
        created_by=1
    )

    db.session.add(the_way_it_ends)
    db.session.commit()

def undo_albums():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM albums"))
        
    db.session.commit()