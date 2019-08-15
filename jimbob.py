import praw
import random
# create the objects from the imported modules

# reddit api login
reddit = praw.Reddit(client_id='redacted',
                     client_secret='redacted',
                     username='SandEnthusiast',
                     password='redacted',
                     user_agent='thisshitdoesntmatterlel')


# the subreddits you want your bot to live on
subreddit = reddit.subreddit('SandLand')

characters = ["Anka", "Annie", "Armin", "Baggy-Pants Leon", "Bertholdt", "General Calvi", "Carla", "Colt", "Connie", "Zachary", "Daz", "The Earth Devil", "Dimo Reeves", "Dina", "Pyxis", "Eld", "Eren Kruger", "Eren", "Erwin", "Falco", "Faye", "Flegel Reeves", "Floch", "Franz", "Freida", "Gabi", "Gelgar", "Grisha", "Gross", "Gunther", "Hange", "Hannah", "Hannes", "Historia", "Hitch", "Ian", "Jean", "Keith","Kenny", "Kitz", "Kiyomi", "Kuchel", "Levi", "Louise", "Marcel", "Marco", "Marlowe", "Mikasa", "Miche", "Mina", "Mitabi", "Mobilt", "Nanaba", "Niccolo", "Pastor Nick", "Nifa", "Nile","Oruo", "Onyankopon", "Petra", "Pieck", "Porco", "Reiner", "Rico", "Rod Reiss", "Rogue", "Sasha", "Magath", "Thomas", "Xaver", "Caven", "Udo", "Uri","Willy Tybur", "Yelena", "Frecklemir", "Lolimir", "Zofia", "Emma Tybur", "Zeke", "Farmer-kun"]
users = ["notabear629", "JustAboutEnoughSpace", "d_140v", "wall-e200", "BIG_DICK_MYSTIQUE", "10messiFH", "Allpaintedbright", "Argus1000", "ArminIsExactlyRight", "Brittneychan", "CHRISTITOonFIRE", "Daylights_New_Hope", "Doom_Hawk", "es452002", "flashlightpoki", "Muckyduck007", "ragnaroksoon", "UnsaturatedSolution", "Verdicious", "Zekes_Coffee_Company", "Valask86", "Taitentai", "Dishout", "hitoribolemon", "WorkerAnt115", "Indigo_Clover", "-V0lD", "YourLocalTeaHoarder", "TheEscapedGoat", "arminfucker69", "NaVENOM", "GhostOfSparta27", "Cloore", "moeyberko"]
living = ["Annie", "Armin", "Baggy-Pants Leon", "Connie", "Daz", "The Earth Devil", "Eren", "Falco", "Flegel Reeves", "Floch", "Gabi", "Hange", "Historia", "Hitch", "Jean", "Keith", "Kitz", "Kiyomi", "Levi", "Louise", "Mikasa", "Niccolo", "Onyankopon", "Pieck", "Reiner", "Rico", "Magath", "Yelena", "Lolimir", "Zeke", "Farmer-kun"]
boys = ["Armin", "Baggy-pants Leon", "Bertholdt", "General Calvi", "Colt", "Connie", "Zachary", "Daz", "Dimo Reeves", "Pyxis", "Eld", "Eren Kruger", "Eren", "Erwin", "Falco", "Flegel Reeves", "Floch", "Franz", "Gelgar", "Grisha", "Gross", "Gunther", "Hannes", "Ian", "Jean", "Keith","Kenny", "Kitz", "Levi", "Marcel", "Marco", "Marlowe", "Miche", "Mitabi", "Mobilt", "Niccolo", "Pastor Nick", "Nile","Oruo", "Onyankopon", "Porco", "Reiner", "Rod Reiss", "Rogue", "Magath", "Thomas", "Xaver", "Udo", "Uri","Willy Tybur", "Zeke", "Farmer-kun"]
girls = ["Anka", "Annie", "Carla", "Dina", "Faye", "Freida", "Gabi", "Hange", "Hannah", "Historia", "Hitch", "Kiyomi", "Kuchel", "Louise", "Mikasa", "Mina", "Nanaba", "Nifa", "Petra", "Pieck", "Rico", "Sasha", "Caven", "Yelena", "Frecklemir", "Lolimir", "Zofia", "Emma Tybur"]
lb = ["Armin", "Baggy-Pants Leon", "Connie", "Daz", "Eren", "Falco", "Flegel Reeves", "Floch", "Jean", "Keith", "Kitz", "Levi", "Niccolo", "Onyankopon", "Reiner", "Zeke", "Farmer-kun", "Magath"]
lg = ["Annie", "Gabi", "Hange", "Historia", "Hitch", "Kiyomi", "Louise", "Mikasa", "Pieck", "Rico", "Yelena", "Lolimir"]

# phrase to activate the bot
rc1 = '!randomcharacter'
rc2 = '?randomcharacter'
rc3 = '+randomcharacter'
rc4 = '-randomcharacter'
rc5 = '$randomcharacter'

ru1 = '!randomuser'
ru2 = '?randomuser'
ru3 = '+randomuser'
ru4 = '-randomuser'
ru5 = '$randomuser'

ra1 = '!randomalive'
ra2 = '?randomalive'
ra3 = '+randomalive'
ra4 = '-randomalive'
ra5 = '$randomalive'

rb1 = '!randomboy'
rb2 = '?randomboy'
rb3 = '+randomboy'
rb4 = '-randomboy'
rb5 = '$randomboy'

rg1 = '!randomgirl'
rg2 = '?randomgirl'
rg3 = '+randomgirl'
rg4 = '-randomgirl'
rg5 = '$randomgirl'

rlb1 = '!randomlivingboy'
rlb2 = '?randomlivingboy'
rlb3 = '+randomlivingboy'
rlb4 = '-randomlivingboy'
rlb5 = '$randomlivingboy'

rlg1 = '!randomlivinggirl'
rlg2 = '?randomlivinggirl'
rlg3 = '+randomlivinggirl'
rlg4 = '-randomlivinggirl'
rlg5 = '$randomlivinggirl'

# look for phrase and reply appropriately

for comment in subreddit.stream.comments():
    if not comment.saved:
        x = "bot machine broke"
       	if ru1 in comment.body:
            if x != "bot machine broke":
                x = x.replace("!randomuser", random.choice(users))
            if x == "bot machine broke":
                x = (comment.body).replace("!randomuser", random.choice(users))
        if ru2 in comment.body:
            x = x.replace("?randomuser", random.choice(users))
        if ru3 in comment.body:
            x = x.replace("+randomuser", random.choice(users))
        if ru4 in comment.body:
            x = x.replace("-randomuser", random.choice(users))
       	if ru5 in comment.body:
            x = x.replace("$randomuser", random.choice(users))
        if ra1 in comment.body:
            if x != "bot machine broke":
                x = x.replace("!randomalive", random.choice(living))
            if x == "bot machine broke":
                x = (comment.body).replace("!randomalive", random.choice(living))
        if ra2 in comment.body:
            x = x.replace("?randomalive", random.choice(living))
        if ra3 in comment.body:
            x = x.replace("+randomalive", random.choice(living))
        if ra4 in comment.body:
            x = x.replace("-randomalive", random.choice(living))
        if ra5 in comment.body:
            x = x.replace("$randomalive", random.choice(living))
        if rb1 in comment.body:
            if x != "bot machine broke":
                x = x.replace("!randomboy", random.choice(users))
            if x == "bot machine broke":
                x = (comment.body).replace("!randomboy", random.choice(boys))
        if rb2 in comment.body:
            x = x.replace("?randomboy", random.choice(boys))
        if rb3 in comment.body:
            x = x.replace("+randomboy", random.choice(boys))
        if rb4 in comment.body:
            x = x.replace("-randomboy", random.choice(boys))
        if rb5 in comment.body:
            x = x.replace("$randomboy", random.choice(boys))
        if rg1 in comment.body:
            if x != "bot machine broke":
                x = x.replace("!randomgirl", random.choice(girls))
            if x == "bot machine broke":
                x = (comment.body).replace("!randomgirl", random.choice(girls))
        if rg2 in comment.body:
            x = x.replace("?randomgirl", random.choice(girls))
        if rg3 in comment.body:
            x = x.replace("+randomgirl", random.choice(girls))
        if rg4 in comment.body:
            x = x.replace("-randomgirl", random.choice(girls))
        if rg5 in comment.body:
            x = x.replace("$randomgirl", random.choice(girls))
        if rlb1 in comment.body:
            if x != "bot machine broke":
                x = x.replace("!randomlivingboy", random.choice(lb))
            if x == "bot machine broke":
                x = (comment.body).replace("!randomlivingboy", random.choice(lb))
        if rlb2 in comment.body:
            x = x.replace("?randomlivingboy", random.choice(lb))
        if rlb3 in comment.body:
            x = x.replace("+randomlivingboy", random.choice(lb))
        if rlb4 in comment.body:
            x = x.replace("-randomlivingboy", random.choice(lb))
        if rlb5 in comment.body:
            x = x.replace("$randomlivingboy", random.choice(lb))
        if rlg1 in comment.body:
            if x != "bot machine broke":
                x = x.replace("!randomlivinggirl", random.choice(lg))
            if x == "bot machine broke":
                x = (comment.body).replace("!randomlivinggirl", random.choice(lg))
        if rlg2 in comment.body:
            x = x.replace("?randomlivinggirl", random.choice(lg))
        if rlg3 in comment.body:
            x = x.replace("+randomlivinggirl", random.choice(lg))
        if rlg4 in comment.body:
            x = x.replace("-randomlivinggirl", random.choice(lg))
        if rlg5 in comment.body:
            x = x.replace("$randomlivinggirl", random.choice(lg))
        if x != "bot machine broke":
            comment.reply(x)
        comment.save()
