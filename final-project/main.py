
from pydoc import Helper
from tracemalloc import start
from piratesonly import Piratesonly

def main():
    print("Hello! Welcome to Pirates Only!\nThe one stop dating shop for every pirate!")
    print("Here are a list of functions you can use to access the database.")
    print("FindUser\tAddMatch\tViewCrew\tViewShip\tViewMatches\tViewPirateMusic\tCommonIntrests\tViewDetails")
    print("If you wish to update some info here are the function names.")
    print("If you are confused on what each function does please type Help")
    print("If you need help with the update functions type helpupdate.")
    print("If you wish to Quit the program type Quit")
    while True:
        po = Piratesonly()
        startinginput = input("Please specify which function to use: ").lower()
        if startinginput == "quit":
            break
        if startinginput == "createuser":
            inp1 = input("First Name?: ")
            inp2 = input("Last Name?: ")
            inp3 = input("Age?: ")
            po.createUser(inp1,inp2,inp3)
            print("Congrats you have signed up for Pirate Only!")
        if startinginput == "finduser":
            inp1 = input("What is the first of name of the person you would like to find? ")
            finduse = po.finduserbyname(inp1)
            print("{:10} {:30} {:30}".format("Pirate Id","First Name","Last Name"))
            print("{:10} {:30} {:30}".format("---","---","---"))
            for i in finduse:
                id = i[0]
                fname = i[1]
                lname = i[2]
                print("{:10} {:30} {:30}".format(str(id),fname,lname))
        if startinginput == "addmatch":
            inp1 = input("Enter your user id: ")
            inp2 = input("Enter the id of the scallywag you matched with: ")
            po.createMatch(inp1,inp2)
            print("Match created!")
        if startinginput == "viewcrew":
            inp = input("Please input which Ship using an id you would like to view the crew for: ")
            crew = po.viewCrew(inp)
            print ("{:<15} {:<15} {:<15} {:<15}".format('Ship Name','First Name','Last Name','Job Title'))
            print ("{:<15} {:<15} {:<15} {:<15}".format('---','---','---','---'))
            for i in crew:
                name, age, perc,job = i
                print ("{:<15} {:<15} {:<15} {:<15}".format( name, age, perc,job))
        if startinginput == "viewship":
            inp = input("Please input which Ship using an id you would like to view the ship info for: ")
            ship = po.viewShip(inp)
            print ("{:30} {:30} {:20}".format('Ship Name',' Captains First Name','Captains Last Name'))
            print ("{:30} {:30} {:20}".format('---','---','---'))
            for i in ship:
                shipname, firstname, lastname = i
                print ("{:30} {:30} {:20}".format( shipname,firstname,lastname))
        if startinginput == "viewmatches":
            inp = input("Please input your pirate id to see who you have matched with!: ")
            matches = po.viewMatches(inp)
            print ("{:30} {:30} {:30} {:30}".format('First Name','Last Name','First Name','Last Name'))
            print ("{:30} {:30} {:30} {:30}".format('---','---','---','---'))
            for i in matches:
                fname1,lname1,fname2,lname2 = i
                print("{:30} {:30} {:30} {:30}".format(fname1,lname1,fname2,lname2))
        if startinginput == "viewpiratemusic":
            print("Here are a list of options: Pirate_Metal,Sea_Shanties,Pirate_Rap,Pirate_Country,Pirate_Techno,Pirate_Folksongs")
            inp = input("Please input which type of music you would like to see that other pirates enjoy! ")
            music = po.viewPiratesMusic(inp)
            print ("{:30} {:30} {:30} {:20}".format('Type of Music','First Name','Last Name','ID'))
            print ("{:30} {:30} {:30} {:20}".format('---','---','---','---'))
            for i in music:
                fname,lname,musicname,id = i
                print ("{:30} {:30} {:30} {:3}".format(fname,lname,musicname,id))
        if startinginput == "viewpiratehobbie":
            print("Here are a list of options: Drinking,Napping,Shooting,Board Games,Stealing,Smoking")
            inp = input("Please input which type of hobbies you would like to see that other pirates enjoy! ")
            music = po.viewPiratesHobbies(inp)
            print ("{:30} {:30} {:30} {:20}".format('hobbies','First Name','Last Name','ID'))
            print ("{:30} {:30} {:30} {:20}".format('---','---','---','---'))
            for i in music:
                fname,lname,hobbie,id = i
                print ("{:30} {:30} {:30} {:3}".format(fname,lname,hobbie,id))
        if startinginput == "viewpirateplunder":
            print("Here are a list of options: Bahamas,Florida,Mexico,Tortuga,Madagascar,Ireland,Italy")
            inp = input("Please input which type of hobbies you would like to see that other pirates enjoy! ")
            music = po.viewPiratesPlunder(inp)
            print ("{:30} {:30} {:30} {:20}".format('Plunder','First Name','Last Name','ID'))
            print ("{:30} {:30} {:30} {:20}".format('---','---','---','---'))
            for i in music:
                fname,lname,plunder,id = i
                print ("{:30} {:30} {:30} {:3}".format(fname,lname,plunder,id))
        if startinginput == "viewdetails":
            inp = input("Please input the id of the user you would like to view. ")
            details = po.viewdetails(inp)
            print ("{:20} {:20} {:20} {:20} {:20}".format('First Name','Last Name','Hobbie','Plunder Spot','Music'))
            print ("{:20} {:20} {:20} {:20} {:20}".format('---','---','---','---','---'))
            for i in details:
                fname = i[0]
                lname = i[1]
                hobbie = i[2]
                plunder = i[3]
                music = i[4]
                print ("{:20} {:20} {:20} {:20} {:20}".format(fname,lname,hobbie,plunder,music))
        if startinginput == "updatemusic":
            inp1 = input("What is the first name of the Pirate? ")
            inp2 = input("What is the last name of the Pirate? ")
            inp3 = input("What genre of music would like to update to? ")
            po.updatepiratemusic(inp3,inp1,inp2)
            print("Music Table succesfully updated!")
        if startinginput == "updateplunder":
            inp1 = input("What is the first name of the Pirate? ")
            inp2 = input("What is the last name of the Pirate? ")
            inp3 = input("What is the place of plunder you wish to change? ")
            po.updatepirateplunder(inp3,inp1,inp2)
            print("Plunder Succesfully updated!")
        if startinginput == "updatehobbies":
            inp1 = input("What is the first name of the Pirate? ")
            inp2 = input("What is the last name of the Pirate? ")
            inp3 = input("What is the hobbie you wish to change? ")
            po.updatepiratehobbie(inp3,inp1,inp2)
            print("Hobbies Succesfully updated!")
        if startinginput == "commonintrests":
            inp = input("Please input an id to see common intrests you and your matches share. ")
            intrests = po.ViewCommonIntrests(inp)
            print ("{:10} {:10} {:20} {:10} {:10} {:10} {:10} {:20} {:10} {:10}".format('first name','last name','music','plunder','hobbie','first name','last name','music','plunder','hobbie'))
            print ("{:10} {:10} {:20} {:10} {:10} {:10} {:10} {:20} {:10} {:10}".format('---','---','---','---','---','---','---','---','---','---'))
            for i in intrests:
                fname = i[0]
                lname = i[1]
                music1 = i[2]
                plunder1 = i[3]
                hobbie1 = i[4]
                fname2 = i[5]
                lname2 = i[6]
                music2 = i[7]
                plunder2 = i[8]
                hobbie2 = i[9]
                print ("{:10} {:10} {:20} {:10} {:10} {:10} {:10} {:20} {:10} {:10}".format(fname,lname,music1,plunder1,hobbie1,fname2,lname2,music2,plunder2,hobbie2))
        if startinginput == "insertintopiratedetails":
            po.insertpiratesdetails()
        if startinginput == "help":
            po.Helpme()
        if startinginput == "helpupdate":
            po.HelpUpdate()
            
           

   

main()



