from app.models import db, Song, environment, SCHEMA
from sqlalchemy import text

def seed_songs():
    # The way it ends
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
    # The death we seek
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
    # aggressive 
    # aggressive = Song(
    #     name='Aggressive',
    #     created_by=2,
    #     album_id=3,
    #     song_body='/Currents-Kill-The-Ache.mp3'
    # )
    # hated = Song(
    #     name='Hated',
    #     created_by=2,
    #     album_id=3,
    #     song_body='/Currents-Kill-The-Ache.mp3'
    # )
    # loser = Song(
    #     name='Loser',
    #     created_by=2,
    #     album_id=3,
    #     song_body='/Currents-Kill-The-Ache.mp3'
    # )
    # fair_weather_friend = Song(
    #     name='Fair Weather Friend',
    #     created_by=2,
    #     album_id=3,
    #     song_body='/Currents-Kill-The-Ache.mp3'
    # )
    # burnout = Song(
    #     name='Burnout',
    #     created_by=2,
    #     album_id=3,
    #     song_body='/Currents-Kill-The-Ache.mp3'
    # )
    # sick_of_me = Song(
    #     name='Sick of Me',
    #     created_by=2,
    #     album_id=3,
    #     song_body='/Currents-Kill-The-Ache.mp3'
    # )
    # censored = Song(
    #     name='Censored',
    #     created_by=2,
    #     album_id=3,
    #     song_body='/Currents-Kill-The-Ache.mp3'
    # )
    # alway_dead = Song(
    #     name='Always Dead',
    #     created_by=2,
    #     album_id=3,
    #     song_body='/Currents-Kill-The-Ache.mp3'
    # )
    # however_you_want_it_said = Song(
    #     name='However You Want it Said',
    #     created_by=2,
    #     album_id=3,
    #     song_body='/Currents-Kill-The-Ache.mp3'
    # )
    # find_a_way = Song(
    #     name='Find a Way',
    #     created_by=2,
    #     album_id=3,
    #     song_body='/Currents-Kill-The-Ache.mp3'
    # )
    # rock_is_dead = Song(
    #     name='Rock is Dead',
    #     created_by=2,
    #     album_id=3,
    #     song_body='/Currents-Kill-The-Ache.mp3'
    # )
    # king_of_anything = Song(
    #     name='King of Anything',
    #     created_by=2,
    #     album_id=3,
    #     song_body='/Currents-Kill-The-Ache.mp3'
    # )
    # color decay
    
    exhibition = Song(
        name='Exhibition',
        created_by=3,
        album_id=3,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Exhibition+TDWP.mp3'
    )
    salt = Song(
        name='Salt',
        created_by=3,
        album_id=3,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Sslt+TDWP.mp3'
    )
    watchtower = Song(
        name='Watchtower',
        created_by=3,
        album_id=3,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Watchtower+TDWP.mp3'
    )
    noise = Song(
        name='Noise',
        created_by=3,
        album_id=3,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Noise+TDWP.mp3'
    )
    broken = Song(
        name='Broken',
        created_by=3,
        album_id=3,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Broken+TDWP.mp3'
    )
    sacrifice = Song(
        name='Sacrifice',
        created_by=3,
        album_id=3,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Sacrafice+TDWP.mp3'
    )
    trapped = Song(
        name='Trapped',
        created_by=3,
        album_id=3,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Trapped+TDWP.mp3'
    )
    time = Song(
        name='Time',
        created_by=3,
        album_id=3,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Time+TDWP.mp3'
    )
    twenty_five = Song(
        name='Twenty Five',
        created_by=3,
        album_id=3,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Twenty-five+TDWP.mp3'
    )
    fire = Song(
        name='Fire',
        created_by=3,
        album_id=3,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Fire+TDWP.mp3'
    )
    hallucinate = Song(
        name='Hallucinate',
        created_by=3,
        album_id=3,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Hallucinate+TDWP.mp3'
    )
    cancer = Song(
        name='Cancer',
        created_by=3,
        album_id=3,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Cancer+TDWP.mp3'
    )
    reaching = Song(
        name='Reaching',
        created_by=3,
        album_id=3,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Reaching+TDWP.mp3'
    )
    ignorance = Song(
        name='Ignorance',
        created_by=3,
        album_id=3,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Ignorance+TDWP.mp3'
    )

    switchblade = Song(
        name='Switchblade',
        created_by=3,
        album_id=4,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Switchblade+TDWP.mp3'
    )
    lines_of_your_hands = Song(
        name='Lines of Your Hands',
        created_by=3,
        album_id=4,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/LInes+of+your+hands+TDWP.mp3'
    )
    chemical = Song(
        name='Chemical',
        created_by=3,
        album_id=4,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Chemical+TDWP.mp3'
    )
    wave_of_youth = Song(
        name='Wave of Youth',
        created_by=3,
        album_id=4,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Wave+of+youth+TDWP.mp3'
    )
    please_say_no = Song(
        name='Please Say No',
        created_by=3,
        album_id=4,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Please+say+no+TDWP.mp3'
    )
    the_thread = Song(
        name='The Thread',
        created_by=3,
        album_id=4,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/The+thread+TDWP.mp3'
    )
    numb = Song(
        name='Numb',
        created_by=3,
        album_id=4,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Numb+TDWP.mp3'
    )
    isnt_it_strange = Song(
        name="Isn't it Strange?",
        created_by=3,
        album_id=4,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Isnt+it+strange+TDWP.mp3'
    )
    diamond_lost = Song(
        name='Diamond Lost',
        created_by=3,
        album_id=4,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Diamong+lost+TDWP.mp3'
    )
    as_kids = Song(
        name='As Kids',
        created_by=3,
        album_id=4,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/As+kids+TDWP.mp3'
    )
    even_though = Song(
        name='Even Though',
        created_by=3,
        album_id=4,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Even+though+TDWP.mp3'
    )
    spiderhead = Song(
        name='Spiderhead',
        created_by=3,
        album_id=4,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Spiderhead+TDWP.mp3'
    )
    godless = Song(
        name='Godless',
        created_by=4,
        album_id=5,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Godless+Angelmaker.mp3'
    )
    no_haven = Song(
        name='No Haven',
        created_by=4,
        album_id=5,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/No+Haven+Angelmaker.mp3'
    )
    a_dark_omen = Song(
        name='A Dark Omen',
        created_by=4,
        album_id=5,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/A+Dark+Omen+Angelmaker.mp3'
    )
    e_i_e = Song(
        name='E.I.E',
        created_by=4,
        album_id=5,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/E.I.E+Angelmaker.mp3'
    )
    dissentient = Song(
        name='Dissentient',
        created_by=4,
        album_id=5,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Dissentient+Angelmaker.mp3'
    )
    citadel = Song(
        name='Citadel',
        created_by=4,
        album_id=5,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Citadel+Angelmaker.mp3'
    )
    shia_labeouf = Song(
        name='Shia Labeouf',
        created_by=4,
        album_id=5,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Shita+LaBeouf+Angelmaker.mp3'
    )
    into_oblivion = Song(
        name='Into Oblivion',
        created_by=4,
        album_id=5,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Into+Oblivion+Angelmaker.mp3'
    )
    abysmal = Song(
        name='Abysmal',
        created_by=4,
        album_id=5,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Abyssal+Angelmaker.mp3'
    )
    leech = Song(
        name='Leech',
        created_by=4,
        album_id=5,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Leech+Angelmaker.mp3'
    )

    concrete_jungle = Song(
        name='CONCRETE JUNGLE',
        created_by=5,
        album_id=6,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/CONCRETE+JUNGLE+Bad+Omens.mp3'
    )
    nowhere_to_go = Song(
        name='Nowhere To Go',
        created_by=5,
        album_id=6,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Nowhere+To+Go+BadOmens.mp3'
    )
    take_me_first = Song(
        name='Take Me First',
        created_by=5,
        album_id=6,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Take+Me+First+BadOmens.mp3'
    )
    the_death_of_peace_of_mind = Song(
        name='THE DEATH OF PEACE OF MIND',
        created_by=5,
        album_id=6,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/THE+DEATH+OF+PEACE+OF+MIND+BadOmens.mp3'
    )
    What_it_cost = Song(
        name='What it Cost',
        created_by=5,
        album_id=6,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/What+it+Cost+BadOmens.mp3'
    )
    like_a_villain = Song(
        name='Like A Villain',
        created_by=5,
        album_id=6,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Like+a+Villain+BadOmens.mp3'
    )
    bad_decisions = Song(
        name='bad decisions',
        created_by=5,
        album_id=6,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Bad+decisions+Bad+Omens.mp3'
    )
    just_pretend = Song(
        name='Just Pretend',
        created_by=5,
        album_id=6,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Just+Pretend+BadOmens.mp3'
    )
    the_grey = Song(
        name='The Grey',
        created_by=5,
        album_id=6,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/The+Grey+BadOmens.mp3'
    )
    who_are_you = Song(
        name='Who are you?',
        created_by=5,
        album_id=6,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Who+are+you+BadOmens.mp3'
    )
    somebody_else = Song(
        name='Somebody else.',
        created_by=5,
        album_id=6,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Sombody+else+BadOmens.mp3'
    )
    idwts = Song(
        name='IDWT$',
        created_by=5,
        album_id=6,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/IDWT%24+BadOmens.mp3'
    )
    what_do_you_want_from_me = Song(
        name='What do you want from me?',
        created_by=5,
        album_id=6,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/What+do+you+want+from+me+BadOmens.mp3'
    )
    artificial_suicide = Song(
        name='ARTIFICIAL SUICIDE',
        created_by=5,
        album_id=6,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/ARTIFICIAL+SUICIDE+BadOmens.mp3'
    )
    miracle = Song(
        name='Miracle',
        created_by=5,
        album_id=6,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Miracle+BadOmens.mp3'
    )

    avgang = Song(
        name='Avgang',
        created_by=6,
        album_id=7,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Avang+Mental+Cruelty.mp3'
    )
    ultima_hypocrita = Song(
        name='Ultima Hypocrita',
        created_by=6,
        album_id=7,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Ultima+Hypcrita+Mental+Cruelty.mp3'
    )
    abadon = Song(
        name='Abadon',
        created_by=6,
        album_id=7,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Abadon+Metal+Cruelty.mp3'
    )
    king_ov_fire = Song(
        name='King Ov Fire',
        created_by=6,
        album_id=7,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/King+Ov+Fire+Mental+Cruelty.mp3'
    )
    eternal_eclipse = Song(
        name='Eternal Eclipse',
        created_by=6,
        album_id=7,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Eternal+Eclipse+Mental+Cruelty.mp3'
    )
    death_worship = Song(
        name='Death Worship',
        created_by=6,
        album_id=7,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Death+Worship+Mental+Cruelty.mp3'
    )
    fossenbrate = Song(
        name='Fossenbrate',
        created_by=6,
        album_id=7,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Fossenbrate+Mental+Cruelty.mp3'
    )
    a_hill_to_die_upon = Song(
        name='A Hill To Die Upon',
        created_by=6,
        album_id=7,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/A+Hill+to+Die+Upon+Mental+Cruelty.mp3'
    )
    extermination_campaign = Song(
        name='Extermination Campaighn',
        created_by=6,
        album_id=7,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Extermination+Campaign+Mental+Cruelty.mp3'
    )
    the_left_hand_path = Song(
        name='The Left Hand Path',
        created_by=6,
        album_id=7,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/The+Left+Hand+Path+Mental+Cruelty.mp3'
    )

    opening_night = Song(
        name='Opening Night...',
        created_by=7,
        album_id=8,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Opening+NIght+INK.mp3'
    )
    welcome_to_horrowood = Song(
        name='Welcome to Horrrowood',
        created_by=7,
        album_id=8,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Ice+Nine+Kills+-+Welcome+To+Horrorwood.mp3'
    )
    a_rash_decision = Song(
        name='A Rash Decision',
        created_by=7,
        album_id=8,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/A+rash+decision+INK.mp3'
    )
    assault_and_batteries = Song(
        name='Assault & Batteries',
        created_by=7,
        album_id=8,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Assault+%26+batteries+INK.mp3'
    )
    the_shower_scene = Song(
        name='The Shower Scene',
        created_by=7,
        album_id=8,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/The+shower+scene+INK.mp3'
    )
    funeral_derangements = Song(
        name='Funeral Derangements',
        created_by=7,
        album_id=8,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Funeral+Derangements+INK.mp3'
    )
    rainy_day = Song(
        name='Rainy Day',
        created_by=7,
        album_id=8,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Rainy+Day+INK.mp3'
    )
    hip_to_be_scared = Song(
        name='Hip to be Scared (feat. Jacoby Shaddix)',
        created_by=7,
        album_id=8,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Hip+to+be+scared+INK.mp3'
    )
    take_your_pick = Song(
        name='Take Your Pick (feat. Corpsegrinder)',
        created_by=7,
        album_id=8,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Take+your+pick+INK.mp3'
    )
    the_box = Song(
        name='The Box (feat. Brandon Saller & Ryan Kirby)',
        created_by=7,
        album_id=8,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/The+box+INK.mp3'
    )
    fly = Song(
        name='F.L.Y. (feat. Buddy Nielsen)',
        created_by=7,
        album_id=8,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/F.L.Y+INK.mp3'
    )
    wurst_vacation = Song(
        name='Wurst Vacations',
        created_by=7,
        album_id=8,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Wurst+Vacation+INK.mp3'
    )
    ex_mortis = Song(
        name='Ex Mørtis',
        created_by=7,
        album_id=8,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Ex-mortis+INK.mp3'
    )
    farewell_to_flesh = Song(
        name='Farewell II Flesh',
        created_by=7,
        album_id=8,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Farewell+II+Flesh+INK.mp3'
    )

    the_american_nightmare = Song(
        name='The American Nightmare',
        created_by=7,
        album_id=9,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Ice+Nine+Kills+-+The+American+Nightmare+(A+Nightmare+On+Elm+Street)+-+HQ+-+Lyrics.mp3'
    )
    thank_got_its_friday = Song(
        name='Thank God It\'s Friday',
        created_by=7,
        album_id=9,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Ice+Nine+Kills+-+Thank+God%2C+It's+Friday+(Friday+The+13th)+-+HQ+-+Lyrics.mp3"
    )
    stabbing_in_the_dark = Song(
        name='Stabbing in the Dark',
        created_by=7,
        album_id=9,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Ice+Nine+Kills+-+Stabbing+In+The+Dark+(Halloween)+-+HQ+-+Lyrics.mp3'
    )
    savages = Song(
        name='SAVAGES',
        created_by=7,
        album_id=9,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Ice+Nine+Kills+-+Savages+(The+Texas+Chainsaw+Massacre)+-+HQ+-+Lyrics.mp3'
    )
    the_jig_is_up = Song(
        name='The Jig is Up (feat. Randy Strohmeyer)',
        created_by=7,
        album_id=9,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Ice+Nine+Kills+-+The+Jig+Is+Up+ft.+Randy+Strohmeyer+(Saw)+-+HQ+-+Lyrics.mp3'
    )
    a_grave_mistake = Song(
        name='A Grave Mistake',
        created_by=7,
        album_id=9,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/A+Grave+Mistake+-+Ice+Nine+Kills+Lyrics.mp3'
    )
    rocking_the_boat = Song(
        name='Rocking the Boat (feat. Jeremy Schwartz)',
        created_by=7,
        album_id=9,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Ice+Nine+Kills+-+Rocking+The+Boat+ft.+Jeremy+Schwartz+(Jaws)+-+HQ+-+Lyrics.mp3'
    )
    enjoy_your_slay = Song(
        name='Enjoy Your Slay (feat. Sam Kubrick)',
        created_by=7,
        album_id=9,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Ice+Nine+Kills+-+Enjoy+your+slay.mp3'
    )
    freak_flag = Song(
        name='Freak Flag',
        created_by=7,
        album_id=9,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Ice+Nine+Kills+-+Freak+Flag+(The+Devil's+Rejects)+-+HQ+-+Lyrics.mp3"
    )
    the_world_in_my_hands = Song(
        name='The World in My Hands (feat. Tony Lovato)',
        created_by=7,
        album_id=9,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Ice+Nine+Kills+-+The+World+In+My+Hands+ft.+Tony+Lovato+(Edward+Scissorhands)+-+HQ+-+Lyrics.mp3'
    )
    merry_axemas = Song(
        name='Merry Axe-mas',
        created_by=7,
        album_id=9,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Ice+Nine+Kills+-+Merry+Axe-Mas+(Silent+Night%2C+Deadly+Night)+-+HQ+-+Lyrics.mp3'
    )
    love_bites = Song(
        name='Love Bites (feat. Chelsea Talmadge)',
        created_by=7,
        album_id=9,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Ice+Nine+Kills+-+Love+Bites+ft.+Chelsea+Talmadge+(An+American+Werewolf+In+London)+-+HQ+-+Lyrics.mp3'
    )
    it_is_the_end = Song(
        name='IT is the End',
        created_by=7,
        album_id=9,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Ice+Nine+Kills+-+IT+Is+The+End+ft.+Peter+Wasilewski+%26+Buddy+Schaub+(Stephen+King's+IT)+-+HQ+-+Lyrics.mp3"
    )
    your_numbers_up = Song(
        name='Your Number\'s Up',
        created_by=7,
        album_id=9,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Ice+Nine+Kills+-+Your+Number's+Up+(Scream)+-+HQ+-+Lyrics.mp3"
    )

    the_nature_of_the_beast = Song(
        name='The Nature of the Beast',
        created_by=7,
        album_id=10,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/The+nature+of+the+beast+INK.mp3"
    )
    communion_of_the_cursed = Song(
        name='Communion of the Cursed',
        created_by=7,
        album_id=10,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Communion+of+the+cursed+INK.mp3"
    )
    bloodbath_and_beyond = Song(
        name='Bloodbath & Beyond',
        created_by=7,
        album_id=10,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Bloodbath+and+Beyond+INK.mp3"
    )
    the_plot_sickens = Song(
        name='The Plot Sickens',
        created_by=7,
        album_id=10,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/The+plot+Sickens+INK.mp3"
    )
    star_crossed_enemies = Song(
        name='Star-Crossed Enemies',
        created_by=7,
        album_id=10,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Star+crossed+enemies+INK.mp3"
    )
    me_myself_and_hyde = Song(
        name='Me, Myself & Hyde',
        created_by=7,
        album_id=10,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Me+myself+and+hyde+INK.mp3"
    )
    alice = Song(
        name='Alice',
        created_by=7,
        album_id=10,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Alice+INK.mp3"
    )
    the_people_in_the_attic = Song(
        name='The People in the Attic',
        created_by=7,
        album_id=10,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/The+people+in+the+attic+INK.mp3"
    )
    Tess_Timony = Song(
        name='Tess-Timony',
        created_by=7,   
        album_id=10,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Tess-Timony+INK.mp3"
    )
    hell_in_the_hallways = Song(
        name='Hell in the Hallways',
        created_by=7,
        album_id=10,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Hell+in+the+hallways+INK.mp3"
    )

    heaven_shall_burn = Song(
        name='Heaven Shall Burn',
        created_by=8,
        album_id=11,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Heaven+shall+burn+Imminence.mp3"
    )
    desolation = Song(
        name='Desolation',
        created_by=8,
        album_id=11,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Desolation+Imminence.mp3"
    )
    come_hell_or_high_water = Song(
        name='Come Hell or High Water',
        created_by=8,
        album_id=11,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Come+hell+or+high+water+imminence.mp3"
    )

    i_am_become_a_name = Song(
        name='I am Become a Name...',
        created_by=8,
        album_id=12,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/I+am+become+a+name+Imminence.mp3"
    )
    ghost = Song(
        name='Ghost',
        created_by=8,
        album_id=12,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Ghost+Imminence.mp3"
    )
    temptation = Song(
        name='Temptation',
        created_by=8,
        album_id=12,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Temptation+Imminence.mp3"
    )
    surrender = Song(
        name='Surrender',
        created_by=8,
        album_id=12,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Surrender+Imminence.mp3"
    )
    chasing_shadows = Song(
        name='Chasing Shadows',
        created_by=8,
        album_id=12,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Chasing+shadows+Imminence.mp3"
    )
    moth_to_a_flame = Song(
        name='Moth to a Flame',
        created_by=8,
        album_id=12,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Moth+to+a+flame+Imminence.mp3"
    )
    alleviate = Song(
        name='Alleviate',
        created_by=8,
        album_id=12,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Alleviate+Imminence.mp3"
    )
    enslaved = Song(
        name='Enslaved',
        created_by=8,
        album_id=12,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Enslaved+Imminence.mp3"
    )
    disappear = Song(
        name='Disappear',
        created_by=8,
        album_id=12,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Dissapear+Imminence.mp3"
    )
    lost_and_left_behind = Song(
        name='Lost and Left Behind',
        created_by=8,
        album_id=12,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Lost+and+left+behing+Imminence.mp3"
    )
    this_too_shall_pass = Song(
        name='این نیز بگذرد',
        created_by=8,
        album_id=12,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/This+too+shall+pass+Imminence.mp3"
    )
    infinity = Song(
        name='∞',
        created_by=8,
        album_id=12,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Infinity+Imminence.mp3"
    )
    heaven_in_hiding = Song(
        name='Heaven in Hiding',
        created_by=8,
        album_id=12,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Heaven+in+hiding+Imminence.mp3"
    )
    jaded = Song(
        name='Jaded',
        created_by=8,
        album_id=12,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Jaded+Imminence.mp3"
    )

    call_me_a_symbol = Song(
        name='Call Me a Symbol',
        created_by=9,
        album_id=13,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Call+me+a+symbol+Jinjer.mp3"
    )
    collosus = Song(
        name='Collosus',
        created_by=9,
        album_id=13,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Colossus+Jinjer.mp3"
    )
    vortex = Song(
        name='Vortex',
        created_by=9,
        album_id=13,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Vortex+Jinjer.mp3"
    )
    disclosure = Song(
        name='Disclosure',
        created_by=9,
        album_id=13,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Disclosure+Jinjer.mp3"
    )
    copy_cat = Song(
        name='Copy Cat',
        created_by=9,
        album_id=13,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Copycat+Jinjer.mp3"
    )
    pearls_and_swine = Song(
        name='Pearls and Swine',
        created_by=9,
        album_id=13,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Pearls+and+Swine+Jinjer.mp3"
    )
    sleep_of_righteous = Song(
        name='Sleep of Righteous',
        created_by=9,
        album_id=13,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Sleep+of+the+Righteous+Jinjer.mp3"
    )
    wallflower = Song(
        name='Wallflower',
        created_by=9,
        album_id=13,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Wallflower+Jinjer.mp3"
    )
    dead_hands_feel_no_pain = Song(
        name='Dead Hands Feel No Pain',
        created_by=9,
        album_id=13,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Dead+hands+feel+no+pain+Jinjer.mp3"
    )
    as_i_boil_ice = Song(
        name='As I Boil Ice',
        created_by=9,
        album_id=13,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/As+I+Boil+Ice+Jinjer.mp3"
    )
    mediator = Song(
        name='Mediator',
        created_by=9,
        album_id=13,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Mediator+Jinjer.mp3"
    )

    on_the_top = Song(
        name='On the Top',
        created_by=9,
        album_id=14,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Jinjer+-+On+The+Top+w+lyrics.mp3'
    )
    pit_of_consciousness = Song(
        name='Pit of Consciousness',
        created_by=9,
        album_id=14,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Jinjer+-+Pit+Of+Consciousness+w+lyrics.mp3'
    )
    judgement_and_punishment = Song(
        name='Judgement (& Punishment)',
        created_by=9,
        album_id=14,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Jinjer+-+Judgement+(%26+Punishment)+w+lyrics.mp3'
    )
    retrospect = Song(
        name='Retrospect',
        created_by=9,
        album_id=14,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Jinjer+-+Retrospection+w+lyrics.mp3'
    )
    pausing_death = Song(
        name='Pausing Death',
        created_by=9,
        album_id=14,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Jinjer+-+Pausing+Death+w+lyrics.mp3'
    )
    noah = Song(
        name='Noah',
        created_by=9,
        album_id=14,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Jinjer+-+Noah+w+lyrics.mp3'
    )
    home_back = Song(
        name='Home Back',
        created_by=9,
        album_id=14,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Jinjer+-+Home+Back+w+lyrics.mp3'
    )
    the_prophecy = Song(
        name='The Prophecy',
        created_by=9,
        album_id=14,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Jinjer+-+The+Prophecy+w+lyrics.mp3'
    )
    lainnerep = Song(
        name='lainnereP',
        created_by=9,
        album_id=14,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/lainnereP.mp3'
    )

    the_end_of_all_we_know = Song(
        name="The End Of All We Know",
        created_by=10,
        album_id=15,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Bleed+from+within+The+End+Of+All+We+Know.mp3"
    )
    pathfinder = Song(
        name="Pathfinder",
        created_by=10,
        album_id=15,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Bleed+from+within+Pathfinder.mp3"
    )
    into_nothing = Song(
        name="Into Nothing",
        created_by=10,
        album_id=15,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Bleed+from+within+Into+Nothing.mp3"
    )
    fall_away = Song(
        name="Fall Away",
        created_by=10,
        album_id=15,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Bleed+from+within+Fall+away.mp3"
    )
    fracture = Song(
        name="Fracture",
        created_by=10,
        album_id=15,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Bleed+from+within+Fracture.mp3"
    )
    night_crossing = Song(
        name='Night Crossing',
        created_by=10,
        album_id=15,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Bleed+from+within+Night+Crossing.mp3"
    )
    for_all_to_see = Song(
        name="For All To See",
        created_by=10,
        album_id=15,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Bleed+from+within+For+all+to+see.mp3"
    )
    ascend = Song(
        name='Ascend',
        created_by=10,
        album_id=15,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Bleed+from+within+Ascend.mp3"
    )
    utopia = Song(
        name='Utopia',
        created_by=10,
        album_id=15,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Bleed+from+within+Utopia.mp3"
    )
    a_depth_that_no_one_dares = Song(
        name="A Depth That No One Dares",
        created_by=10,
        album_id=15,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Bleed+from+within+A+depth+that+no+one+dares.mp3"
    )

    insert_coin = Song(
        name='Insert Coin',
        created_by=11,
        album_id=16,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Slipknot+insert+coin.mp3"
    )
    unsainted = Song(
        name='Unsainted',
        created_by=11,
        album_id=16,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Slipknot+Unstainted.mp3"
    )
    Birth_of_the_cruel = Song(
        name="Birth of the Cruel",
        created_by=11,
        album_id=16,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Slipknot+Birth+of+the+curel.mp3"
    )
    death_because_of_death = Song(
        name="Death Because of Death",
        created_by=11,
        album_id=16,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Slipknot+Death+because+of+death.mp3"
    )
    nero_forte = Song(
        name="Nero Forte",
        created_by=11,
        album_id=16,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Slipknot+Neo+forte.mp3"
    )
    critical_darling = Song(
        name="Critical Darling",
        created_by=11,
        album_id=16,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Slipknot+Critical+Darling.mp3"
    )
    a_liars_funeral = Song(
        name="A Liar's Funeral",
        created_by=11,
        album_id=16,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Slipknot+A+liars+funeral.mp3"
    )
    red_flag = Song(
        name="Red Flag",
        created_by=11,
        album_id=16,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Slipknot+Red+flag.mp3"
    )
    spiders = Song(
        name="Spiders",
        created_by=11,
        album_id=16,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Slipknot+Spiders.mp3"
    )
    whats_next = Song(
        name="What's Next",
        created_by=11,
        album_id=16,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Slipknot+Whats+next.mp3'
    )
    orphan = Song(
        name="Orphan",
        created_by=11,
        album_id=16,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Slipknot+Orphan.mp3"
    )
    my_pain = Song(
        name="My Pain",
        created_by=11,
        album_id=16,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Slipknot+My+pain.mp3"
    )
    not_long_for_this_world = Song(
        name="Not Long for This World",
        created_by=11,
        album_id=16,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Slipknot+Not+long+for+this+world.mp3'
    )
    solway_firth = Song(
        name="Solway Firth",
        created_by=11,
        album_id=16,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Slipknot+Solway+Firth.mp3"
    )
    all_out_life = Song(
        name="All Out Life",
        created_by=11,
        album_id=16,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Slipknot+All+out+life.mp3"
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

    # db.session.add(aggressive)
    # db.session.add(hated)
    # db.session.add(loser)
    # db.session.add(fair_weather_friend)
    # db.session.add(burnout)
    # db.session.add(sick_of_me)
    # db.session.add(censored)
    # db.session.add(alway_dead)
    # db.session.add(however_you_want_it_said)
    # db.session.add(find_a_way)
    # db.session.add(rock_is_dead)
    # db.session.add(king_of_anything)

    db.session.add(exhibition)
    db.session.add(salt)
    db.session.add(watchtower)
    db.session.add(noise)
    db.session.add(broken)
    db.session.add(sacrifice)
    db.session.add(trapped)
    db.session.add(time)
    db.session.add(twenty_five)
    db.session.add(fire)
    db.session.add(hallucinate)
    db.session.add(cancer)
    db.session.add(reaching)
    db.session.add(ignorance)

    db.session.add(switchblade)
    db.session.add(lines_of_your_hands)
    db.session.add(chemical)
    db.session.add(wave_of_youth)
    db.session.add(please_say_no)
    db.session.add(the_thread)
    db.session.add(numb)
    db.session.add(isnt_it_strange)
    db.session.add(diamond_lost)
    db.session.add(as_kids)
    db.session.add(even_though)
    db.session.add(spiderhead)

    db.session.add(godless)
    db.session.add(no_haven)
    db.session.add(a_dark_omen)
    db.session.add(e_i_e)
    db.session.add(dissentient)
    db.session.add(citadel)
    db.session.add(shia_labeouf)
    db.session.add(into_oblivion)
    db.session.add(abysmal)
    db.session.add(leech)

    db.session.add(concrete_jungle)
    db.session.add(nowhere_to_go)
    db.session.add(take_me_first)
    db.session.add(the_death_of_peace_of_mind)
    db.session.add(What_it_cost)
    db.session.add(like_a_villain)
    db.session.add(bad_decisions)
    db.session.add(just_pretend)
    db.session.add(the_grey)
    db.session.add(who_are_you)
    db.session.add(somebody_else)
    db.session.add(idwts)
    db.session.add(what_do_you_want_from_me)
    db.session.add(artificial_suicide)
    db.session.add(miracle)

    db.session.add(avgang)
    db.session.add(ultima_hypocrita)
    db.session.add(abadon)
    db.session.add(king_ov_fire)
    db.session.add(eternal_eclipse)
    db.session.add(death_worship)
    db.session.add(fossenbrate)
    db.session.add(a_hill_to_die_upon)
    db.session.add(extermination_campaign)
    db.session.add(the_left_hand_path)

    db.session.add(opening_night)
    db.session.add(welcome_to_horrowood)
    db.session.add(a_rash_decision)
    db.session.add(assault_and_batteries)
    db.session.add(the_shower_scene)
    db.session.add(funeral_derangements)
    db.session.add(rainy_day)
    db.session.add(hip_to_be_scared)
    db.session.add(take_me_first)
    db.session.add(take_your_pick)
    db.session.add(the_box)
    db.session.add(fly)
    db.session.add(wurst_vacation)
    db.session.add(ex_mortis)
    db.session.add(farewell_to_flesh)

    db.session.add(the_american_nightmare)
    db.session.add(thank_got_its_friday)
    db.session.add(stabbing_in_the_dark)
    db.session.add(savages)
    db.session.add(the_jig_is_up)
    db.session.add(a_grave_mistake)
    db.session.add(rocking_the_boat)
    db.session.add(enjoy_your_slay)
    db.session.add(freak_flag)
    db.session.add(the_world_in_my_hands)
    db.session.add(merry_axemas)
    db.session.add(love_bites)
    db.session.add(it_is_the_end)
    db.session.add(your_numbers_up)

    db.session.add(the_nature_of_the_beast)
    db.session.add(communion_of_the_cursed)
    db.session.add(bloodbath_and_beyond)
    db.session.add(the_plot_sickens)
    db.session.add(star_crossed_enemies)
    db.session.add(me_myself_and_hyde)
    db.session.add(alice)
    db.session.add(the_people_in_the_attic)
    db.session.add(Tess_Timony)
    db.session.add(hell_in_the_hallways)

    db.session.add(heaven_shall_burn)
    db.session.add(desolation)
    db.session.add(come_hell_or_high_water)

    db.session.add(i_am_become_a_name)
    db.session.add(ghost)
    db.session.add(temptation)
    db.session.add(surrender)
    db.session.add(chasing_shadows)
    db.session.add(moth_to_a_flame)
    db.session.add(alleviate)
    db.session.add(enslaved)
    db.session.add(disappear)
    db.session.add(lost_and_left_behind)
    db.session.add(this_too_shall_pass)
    db.session.add(infinity)
    db.session.add(heaven_in_hiding)
    db.session.add(jaded)

    db.session.add(call_me_a_symbol)
    db.session.add(collosus)
    db.session.add(vortex)
    db.session.add(disclosure)
    db.session.add(copy_cat)
    db.session.add(pearls_and_swine)
    db.session.add(sleep_of_righteous)
    db.session.add(wallflower)
    db.session.add(dead_hands_feel_no_pain)
    db.session.add(as_i_boil_ice)
    db.session.add(mediator)

    db.session.add(on_the_top)
    db.session.add(pit_of_consciousness)
    db.session.add(judgement_and_punishment)
    db.session.add(retrospect)
    db.session.add(pausing_death)
    db.session.add(noah)
    db.session.add(home_back)
    db.session.add(the_prophecy)
    db.session.add(lainnerep)

    db.session.add(the_end_of_all_we_know)
    db.session.add(pathfinder)
    db.session.add(into_nothing)
    db.session.add(fall_away)
    db.session.add(fracture)
    db.session.add(night_crossing)
    db.session.add(for_all_to_see)
    db.session.add(ascend)
    db.session.add(utopia)
    db.session.add(a_depth_that_no_one_dares)

    db.session.add(insert_coin)
    db.session.add(unsainted)
    db.session.add(Birth_of_the_cruel)
    db.session.add(death_because_of_death)
    db.session.add(nero_forte)
    db.session.add(critical_darling)
    db.session.add(a_liars_funeral)
    db.session.add(red_flag)
    db.session.add(whats_next)
    db.session.add(spiders)
    db.session.add(orphan)
    db.session.add(my_pain)
    db.session.add(not_long_for_this_world)
    db.session.add(solway_firth)
    db.session.add(all_out_life)

    db.session.commit()

def undo_songs():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM songs"))
        
    db.session.commit()