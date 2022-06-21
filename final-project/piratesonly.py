import sqlite3
import random
import sys

class Piratesonly:

    def __init__(self):
        self.connection = sqlite3.connect("database.db")
        self.cursor = self.connection.cursor()

    def createUser(self,first_name,last_name,age):
        data = [first_name,last_name,age]
        self.cursor.execute("INSERT INTO pirates (first_name, last_name, age) VALUES (?,?,?)",data)
        self.connection.commit()

    def finduserbyname(self,firstname):
        data = [firstname]
        self.cursor.execute("SELECT id,first_name,last_name FROM pirates WHERE first_name = ?",data)
        return self.cursor.fetchall()

    def createMatch(self,id,matchedid):
        data = [id,matchedid]
        self.cursor.execute("INSERT INTO hearties (pirate_id,matched_id) VALUES (?,?)",data)
        self.connection.commit()

    def updatepiratemusic(self,music,fname,lname):
        data = [music,fname,lname]
        self.cursor.execute("""
        UPDATE pirate_details SET fav_pirate_music = ?
        WHERE pirate_id IN (SELECT id FROM pirates WHERE first_name = ? AND last_name = ?)
         """,data)

        # UPDATE pirate_details SET fav_pirate_music = 'Sea Shanties'
        # WHERE pirate_id IN (SELECT id FROM pirates WHERE first_name = 'Thunder' AND last_name = 'Dave')

    def updatepirateplunder(self,plunder,fname,lname):
        data = [plunder,fname,lname]
        self.cursor.execute("""
        UPDATE pirate_details SET fav_place_to_plunder = ?
        WHERE pirate_id IN (SELECT id FROM pirates WHERE first_name = ? AND last_name = ?)
         """,data)

    def updatepiratehobbie(self,hobbie,fname,lname):
        data = [hobbie,fname,lname]
        self.cursor.execute("""
        UPDATE pirate_details SET pirate_hobbies = ?
        WHERE pirate_id IN (SELECT id FROM pirates WHERE first_name = ? AND last_name = ?)
         """,data)

    def viewShip(self,id):
        data = [id]
        self.cursor.execute("SELECT ships.name AS name_of_ship,pirates.first_name AS captain_first_name,pirates.last_name AS captains_last_name FROM ships JOIN pirates ON ships.captain_id = pirates.id WHERE ships.boat_id = ?",data)
        return self.cursor.fetchall()

    # view crew members on a certain ship.
    def viewCrew(self,id):
        data = [id]
        self.cursor.execute("""
        SELECT ships.name AS name_of_ship, pirates.first_name AS pirates_first_name, pirates.last_name AS pirates_last_name,crew.job_title
        FROM ships JOIN crew ON ships.boat_id = crew.boat_id 
        JOIN pirates on crew.pirate_id = pirates.id WHERE ships.boat_id = ?
        """,data)
        return self.cursor.fetchall()

    def createPirateDetails(self,id,hobbies,plunder,music):
        data = [id,hobbies,plunder,music]
        self.cursor.execute("INSERT INTO pirate_details (pirate_id,pirate_hobbies,fav_place_to_plunder,fav_pirate_music) VALUES (?,?,?,?)",data)
        self.connection.commit()

    def viewMatches(self,id):
        data = [id]
        self.cursor.execute("SELECT pirates.first_name,pirates.last_name,p.first_name,p.last_name FROM pirates JOIN hearties ON hearties.pirate_id = pirates.id JOIN pirates AS p ON p.id = hearties.matched_id WHERE pirates.id = ?",data)
        return self.cursor.fetchall()

    def viewdetails(self,id):
        data = [id]
        self.cursor.execute("""
        SELECT pirates.first_name,pirates.last_name,pirate_details.pirate_hobbies,pirate_details.fav_place_to_plunder,pirate_details.fav_pirate_music
        FROM pirates 
        JOIN pirate_details ON pirate_details.pirate_id = pirates.id
        WHERE pirates.id = ?
        """,data)
        return self.cursor.fetchall()

    def viewPiratesHobbies(self,hobbie):
        data = [hobbie]
        self.cursor.execute("""SELECT pirate_details.pirate_hobbies,p.first_name,p.last_name,p.id 
        FROM pirate_details 
        JOIN pirates AS p ON pirate_details.pirate_id = p.id 
        WHERE pirate_details.pirate_hobbies = ?
        """,data) 
        return self.cursor.fetchall()

    def viewPiratesPlunder(self,plunder):
        data = [plunder]
        self.cursor.execute("""SELECT pirate_details.fav_place_to_plunder,p.first_name,p.last_name,p.id 
        FROM pirate_details 
        JOIN pirates AS p ON pirate_details.pirate_id = p.id 
        WHERE pirate_details.fav_place_to_plunder = ?
        """,data) 
        return self.cursor.fetchall()
    # find pirates with the same favorite music.
    def viewPiratesMusic(self,favmusic):
        data = [favmusic]
        self.cursor.execute("""SELECT pirate_details.fav_pirate_music,p.first_name,p.last_name,p.id 
        FROM pirate_details 
        JOIN pirates AS p ON pirate_details.pirate_id = p.id 
        WHERE pirate_details.fav_pirate_music = ?
        """,data) 
        return self.cursor.fetchall()

    def insertpiratesdetails(self):
        pirate_hobbie = ["Drinking","Napping","Shooting","Board Games","Stealing","Smoking"]
        pirate_plunder = ["Bahamas","Florida","Mexico","Tortuga","Madagascar","Ireland","Italy"]
        pirate_music = ["Pirate_Metal","Sea_Shanties","Pirate_Rap","Pirate_Country","Pirate_Techno","Pirate_Folksongs"]
        for i in range(0,129):
            i += 1
            fav_plunder = random.choice(pirate_plunder)
            fav_hobbie = random.choice(pirate_hobbie)
            fav_music = random.choice(pirate_music)
            pirate_age = random.randint(18,40)
            data = [i,fav_hobbie,fav_plunder,fav_music,pirate_age]
            self.cursor.execute("INSERT INTO pirate_details (pirate_id,pirate_hobbies,fav_place_to_plunder,fav_pirate_music,pirate_age) VALUES (?,?,?,?,?)",data)
        self.connection.commit()
    
    def ViewCommonIntrests(self,id):
        data = [id]
        self.cursor.execute("""
        SELECT p.first_name,p.last_name,details.fav_pirate_music,details.fav_place_to_plunder,details.pirate_hobbies,p2.first_name,p2.last_name,details2.fav_pirate_music,details2.fav_place_to_plunder,details2.pirate_hobbies
        FROM pirates AS p
        JOIN pirate_details AS details on p.id = details.pirate_id 
        JOIN hearties AS matches ON matches.pirate_id  = p.id 
        JOIN pirates AS p2 ON p2.id = matches.matched_id
        JOIN pirate_details AS details2 ON p2.id = details2.pirate_id
        WHERE p.id = ?
        AND p.id <> p2.id
        AND (details.fav_pirate_music = details2.fav_pirate_music
        OR details.pirate_hobbies = details2.pirate_hobbies
        OR details.fav_place_to_plunder = details2.fav_place_to_plunder)
        """,data)
        return self.cursor.fetchall()


    def Helpme(self):
        print("Thanks for seeking help! Here are a list options to choose from")
        print("CreateUser: This functions adds a new pirate.")
        print("ViewShip: This function lets the user view ships name and also the name of the captain.")
        print("ViewCrew: This function lets the user view the crew from a ship of their choosing.")
        print("ViewMatches: This function lets the user view all of their matches.")
        print("ViewPiratesMusic: This function lets you view other pirates that have a similar taste in music.")
        print("CommonIntrests: This function allows the users to see what common intrests they have with their matches.")
        print("ViewDetails: Lets the user view the details of a certain pirate using an id. ")
        print("AddMatch: This function takes in a user id and the id of the pirate you wish to match with and adds it to the database.")

    def HelpUpdate(self):
        print("UpdateMusic can be updated using these genres.\nPirate_Metal,Sea_Shanties,Pirate_Rap,Pirate_Country,Pirate_Techno,Pirate_Folksongs\n")
        print("UpdatePlunder can be updated using these places.\nBahamas,Florida,Mexico,Tortuga,Madagascar,Ireland,Italy\n")
        print("UpdateHobbies can be updated using these hobbies.\nDrinking,Napping,Shooting,Board Games,Stealing,Smoking\n")