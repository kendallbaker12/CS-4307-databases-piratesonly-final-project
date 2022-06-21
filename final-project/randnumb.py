import random

# implement this into an insert statement.
hobbie = ["Drinking","Napping","Shooting","Board Games","Stealing","Smoking"]
plunder = ["Bahamas","Florida","Mexico","Tortuga","Madagascar","Ireland","Italy"]
music = ["Pirate_Metal","Sea_Shanties","Pirate_Rap","Pirate_Country","Pirate_Techno","Pirate_Folksongs"]
id = 0
# for i in range(167):
#     id += 1
#     fav_plunder = random.choice(plunder)
#     fav_hobbie = random.choice(hobbie)
#     fav_music = random.choice(music)
#     age = random.randint(18,40)
#     hearties = id,fav_plunder,fav_hobbie,fav_music,age
with open('piratedetails.txt','w') as f:
    for i in range(167):
        id += 1
        fav_plunder = random.choice(plunder)
        fav_hobbie = random.choice(hobbie)
        fav_music = random.choice(music)
        age = random.randint(18,40)
        hearties = id,fav_plunder,fav_hobbie,fav_music,age
        f.write(str(hearties))
        f.write('\n')


