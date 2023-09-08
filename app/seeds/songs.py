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
        created_by=8,
        album_id=9,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Ice+Nine+Kills+-+The+American+Nightmare+(A+Nightmare+On+Elm+Street)+-+HQ+-+Lyrics.mp3'
    )
    thank_got_its_friday = Song(
        name='Thank God It\'s Friday',
        created_by=8,
        album_id=9,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Ice+Nine+Kills+-+Thank+God%2C+It's+Friday+(Friday+The+13th)+-+HQ+-+Lyrics.mp3"
    )
    stabbing_in_the_dark = Song(
        name='Stabbing in the Dark',
        created_by=8,
        album_id=9,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Ice+Nine+Kills+-+Stabbing+In+The+Dark+(Halloween)+-+HQ+-+Lyrics.mp3'
    )
    savages = Song(
        name='SAVAGES',
        created_by=8,
        album_id=9,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Ice+Nine+Kills+-+Savages+(The+Texas+Chainsaw+Massacre)+-+HQ+-+Lyrics.mp3'
    )
    the_jig_is_up = Song(
        name='The Jig is Up (feat. Randy Strohmeyer)',
        created_by=8,
        album_id=9,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Ice+Nine+Kills+-+The+Jig+Is+Up+ft.+Randy+Strohmeyer+(Saw)+-+HQ+-+Lyrics.mp3'
    )
    a_grave_mistake = Song(
        name='A Grave Mistake',
        created_by=8,
        album_id=9,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/A+Grave+Mistake+-+Ice+Nine+Kills+Lyrics.mp3'
    )
    rocking_the_boat = Song(
        name='Rocking the Boat (feat. Jeremy Schwartz)',
        created_by=8,
        album_id=9,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Ice+Nine+Kills+-+Rocking+The+Boat+ft.+Jeremy+Schwartz+(Jaws)+-+HQ+-+Lyrics.mp3'
    )
    enjoy_your_slay = Song(
        name='Enjoy Your Slay (feat. Sam Kubrick)',
        created_by=8,
        album_id=9,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Ice+Nine+Kills+-+Enjoy+your+slay.mp3'
    )
    freak_flag = Song(
        name='Freak Flag',
        created_by=8,
        album_id=9,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Ice+Nine+Kills+-+Freak+Flag+(The+Devil's+Rejects)+-+HQ+-+Lyrics.mp3"
    )
    the_world_in_my_hands = Song(
        name='The World in My Hands (feat. Tony Lovato)',
        created_by=8,
        album_id=9,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Ice+Nine+Kills+-+The+World+In+My+Hands+ft.+Tony+Lovato+(Edward+Scissorhands)+-+HQ+-+Lyrics.mp3'
    )
    merry_axemas = Song(
        name='Merry Axe-mas',
        created_by=8,
        album_id=9,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Ice+Nine+Kills+-+Merry+Axe-Mas+(Silent+Night%2C+Deadly+Night)+-+HQ+-+Lyrics.mp3'
    )
    love_bites = Song(
        name='Love Bites (feat. Chelsea Talmadge)',
        created_by=8,
        album_id=9,
        song_body='https://tritone-spotify-clone.s3.amazonaws.com/Ice+Nine+Kills+-+Love+Bites+ft.+Chelsea+Talmadge+(An+American+Werewolf+In+London)+-+HQ+-+Lyrics.mp3'
    )
    it_is_the_end = Song(
        name='IT is the End (feat. Less Than Jake, Fenix TX, JR Wasilewski, Buddy Schaub & Will Salazar)',
        created_by=8,
        album_id=9,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Ice+Nine+Kills+-+IT+Is+The+End+ft.+Peter+Wasilewski+%26+Buddy+Schaub+(Stephen+King's+IT)+-+HQ+-+Lyrics.mp3"
    )
    your_numbers_up = Song(
        name='Your Number\'s Up',
        created_by=8,
        album_id=9,
        song_body="https://tritone-spotify-clone.s3.amazonaws.com/Ice+Nine+Kills+-+Your+Number's+Up+(Scream)+-+HQ+-+Lyrics.mp3"
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

    db.session.commit()

def undo_songs():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM songs"))
        
    db.session.commit()