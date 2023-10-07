from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_users():
    currents = User(
        username='Currents',
        email='currents@aa.io',
        first_name='currents',
        last_name='currents',
        password='password'
    )
    beartooth = User(
        username='Beartooth',
        email='beartooth@aa.io',
        first_name='Beartooth',
        last_name='Beartooth',
        password='password'
    )
    tdwp = User(
        username='The Devil Wears Prada',
        email='tdwp@aa.io',
        first_name='The devil',
        last_name='Wears Prada',
        password='password'
    )
    angelmaker = User(
        username='Angelmaker',
        email='angelmaker@aa.io',
        first_name='Angel',
        last_name='maker',
        password='password'
    )
    bad_omens = User(
        username='Bad Omens',
        email='badOmens@aa.io',
        first_name='Bad',
        last_name='Omens',
        password='password'
    )
    mental_cruelty = User(
        username='Mental Cruelty',
        email='mentalCruelty@aa.io',
        first_name='Mental',
        last_name='Cruelty',
        password='password'
    )
    bleed_from_within = User(
        username='Bleed From Within',
        email='bfw@aa.io',
        first_name='Bleed from',
        last_name='Within',
        password='password'
    )
    ice_nine_kills = User(
        username='Ice Nine Kills',
        email='ink@aa.io',
        first_name='Ice Nine',
        last_name='Kills',
        password='YaLikeIceNineKills?'
    )
    imminence = User(
        username='Imminence',
        email='imminence@aa.io',
        first_name='Imm',
        last_name='inence',
        password='password'
    )
    jinjer = User(
        username='Jinjer',
        email='jinjer@aa.io',
        first_name='Jin',
        last_name='Jer',
        password='password'
    )
    slipknot = User(
        username="Slipknot",
        email='slipknot@aa.io',
        first_name='Slip',
        last_name='Knot',
        password='password'
    )
    demo = User(
        username='Demo', 
        email='demo@aa.io', 
        first_name='Demo', 
        last_name='Lition', 
        password='password')
    marnie = User(
        username='marnie', 
        email='marnie@aa.io', 
        first_name='Marnie', 
        last_name='Sue', 
        password='password')
    bobbie = User(
        username='bobbie', 
        email='bobbie@aa.io',
        first_name='Bobbie', 
        last_name='Bob', 
        password='password')

    db.session.add(currents)
    db.session.add(beartooth)
    db.session.add(tdwp)
    db.session.add(angelmaker)
    db.session.add(bad_omens)
    db.session.add(mental_cruelty)
    db.session.add(ice_nine_kills)
    db.session.add(imminence)
    db.session.add(jinjer)
    db.session.add(bleed_from_within)
    db.session.add(slipknot)
    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))
        
    db.session.commit()