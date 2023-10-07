from app.models import db, Album, environment, SCHEMA
from sqlalchemy import text

def seed_albums():
    the_way_it_ends = Album(
        name='The Way It Ends',
        created_by_id=1,
        art='/Currents-the-way-it-ends.jpg'
    )
    the_death_we_seek = Album(
        name='The Death We Seek',
        created_by_id=1,
        art='https://tritone-spotify-clone.s3.amazonaws.com/The-death-we-seak-album-cover.jpg'
    )
    aggressive = Album(
        name='Aggressive',
        created_by_id=2,
        art='/Beartooth-aggressive.jpg'
    )
    color_decay = Album(
        name='Color Decay',
        created_by_id=3,
        art='/TDWP-color-decay.jpg'
    )
    the_act = Album(
        name='The Act',
        created_by_id=3,
        art='https://tritone-spotify-clone.s3.amazonaws.com/Theact.jpg'
    )
    dissentient = Album(
        name='dissentient',
        created_by_id=4,
        art='/Angelmaker-dissentient.jpg'
    )
    angelmaker_self_titled = Album(
        name='Angelmaker',
        created_by_id=4,
        art='/Angelmaker-dissentient.jpg'
    )
    the_death_of_peace_of_mind = Album(
        name='THE DEATH OF PEACE OF MIND',
        created_by_id=5,
        art='/Bad-omens-the-death-of-peace-of-mind.png'
    )
    bad_omens_self_titled = Album(
        name='Bad Omens',
        created_by_id=5,
        art='/Bad-omens-the-death-of-peace-of-mind.png'
    )
    a_hill_to_die_upon = Album(
        name='A Hill To Die Upon',
        created_by_id=6,
        art='https://tritone-spotify-clone.s3.amazonaws.com/A+hill+to+die++upon+art+Mental+Cureltyjpg.jpg'
    )
    the_silver_scream_2 = Album(
        name='Welcome to Horrorwood: The Silver Scream 2',
        created_by_id=7,
        art='https://tritone-spotify-clone.s3.amazonaws.com/INK+The+silver+scream+2.jpg'
    )
    the_silver_scream = Album(
        name='The Silver Scream',
        created_by_id=7,
        art="https://tritone-spotify-clone.s3.amazonaws.com/Ice_Nine_Kills_%E2%80%93_The_Silver_Scream.png"
    )
    every_trick_in_the_book = Album(
        name='Every Trick In The Book',
        created_by_id=7,
        art='https://tritone-spotify-clone.s3.amazonaws.com/Every+Trick+in+the+book+INK.jpg'
    )
    heaven_shall_burn = Album(
        name='Heaven Shall Burn',
        created_by_id=8,
        art='https://tritone-spotify-clone.s3.amazonaws.com/Heaven+Shall+Burn+Art+Imminence.png'
    )
    heaven_in_hiding = Album(
        name='Heaven in Hiding',
        created_by_id=8,
        art='https://tritone-spotify-clone.s3.amazonaws.com/Heaven+in+hiding+art.jpg'
    )
    wallflowers = Album(
        name = 'Wallflowers',
        created_by_id=9,
        art='https://tritone-spotify-clone.s3.amazonaws.com/Wallflowers+art+JINJER.jpg'
    )
    macro = Album(
        name='Macro',
        created_by_id=9,
        art='https://tritone-spotify-clone.s3.amazonaws.com/Macro+art+Jinjer.jpg'
    )
    fracture = Album(
        name='Fracture',
        created_by_id=10,
        art='https://tritone-spotify-clone.s3.amazonaws.com/Fracture-Bleed-From-Within+art.jpg'
    )
    we_are_not_your_kind = Album(
        name='We Are Not Your Kind',
        created_by_id=11,
        art='https://tritone-spotify-clone.s3.amazonaws.com/Wank+ablum+art.jpg'
    )
    iowa = Album(
        name="Iowa",
        created_by_id=11,
        art="https://tritone-spotify-clone.s3.amazonaws.com/Slipknot_Iowa.jpg"
    )

    db.session.add(the_way_it_ends)
    db.session.add(the_death_we_seek)
    # db.session.add(aggressive)
    db.session.add(color_decay)
    db.session.add(the_act)
    db.session.add(dissentient)
    # db.session.add(angelmaker_self_titled)
    db.session.add(the_death_of_peace_of_mind)
    db.session.add(a_hill_to_die_upon)
    # db.session.add(bad_omens_self_titled)
    db.session.add(the_silver_scream_2)
    db.session.add(the_silver_scream)
    db.session.add(every_trick_in_the_book)
    db.session.add(heaven_shall_burn)
    db.session.add(heaven_in_hiding)
    db.session.add(wallflowers)
    db.session.add(macro)
    db.session.add(fracture)
    db.session.add(we_are_not_your_kind)
    # db.session.add(iowa)
    db.session.commit()

def undo_albums():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM albums"))
        
    db.session.commit()