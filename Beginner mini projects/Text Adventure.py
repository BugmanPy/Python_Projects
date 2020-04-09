'''*************************************************************************
NAME: Text Adventure
DISCRIPTION: A begenner python project that create a text based adventure
             game
CREATED BY: Thejus S
DATE OF CREATION: 08 Apr 2020
MODIFIED: -
*************************************************************************'''
##-- Global variables --##
smith = 0
doorKey = 0
smithKey = 0
hammer = 0
position = 0
guard1 = 1
guard2 = 1
csDoor = 0

def main():
    print()
    print("""Welcome Agent!
    You are entrusted with the task of saving Mr.Smith who has been
    kept captive in a ware house building. We have managed to
    infiltrate you into the garage of the warehouse. Find you way from
    here on. Good Luck! """)
    print("----------------------------------------------------------------")

    garage()



#Garage room with position value 1
def garage():
    print("----------------------------------------------------------------")
    global hammer #Uses global variable to track tools
    global position #Uses position as global variable to track player
                    # location
    ##-- Prints a custum message based on player position --##
    if (position == 0):
        print("You have entere the garage.")
        print("Good Luck!")
    elif (position == 3):
        print("You entered garage from Storage 2.")
    elif (position == 2):
        print("You entered garage from Storage 1")
    print()

    position = 1 #Changes the position value to garage
    print(""" > Vehicle in repair in the middle of the room
	\r > On the middle of the west wall there is a door saying
	 "Storage 2"
	\r > On the far north there is a door saying "storage 1"
	\r > On the nort eastern side, close to the east wall, there
	 are some vehicle parts bundled.
	\r > On the nortn Western corner there is a tools table""")

    ##-- Prompts the player for actions --#
    rept = True
    while rept:
        print()
        action = input("""What's your action?
        \r 1. Open Storage 1
    	\r 2. Open Storage 2
    	\r 3. Explore Vehicle parts
    	\r 4. Explore tools table \n""")
        print()
        if (action == '1'):
            rept = False
            storage1()
        elif (action == '2'):
            rept = False
            storage2()
        elif (action == '3'):
            print("There is nothing here.")
        elif (action == '4'):
            if (hammer == 0): #Checks weather the player alredy has tools
                hammer = 1 #Picks up the hammer, globally
                print("You have found a hammer. This might be useful.")
            else:
                print(" You have already explored it.")



#Storage 1 with position value 2
def storage1():
    print("----------------------------------------------------------------")
    global hammer #Uses global variable to track tools
    global doorKey #Uses global variable to track door key
    global position #Uses position as global variable to track player
                    # location
    ##-- Prints a custum message based on player position --##
    if (position == 1):
        print("You have entered storage 1 from garage.")
    elif (position == 4):
        print("You entered storage 1 from shipments.")
    print()
    position = 2

    print(""" > Appears abandoned
	\r > A table on the north eastern corner
	\r > Window in the middle of eastern wall
	\r > Door, a little towards south from the middle of the
	 western wall saying \"Shipments\"
    \r > A door on the south wall saying "Garage".""")

    ##-- Prompts the player for actions --#
    rept = True
    while rept:
        print()
        action = input("""What's your action?
          \r 1. Open Shipments
    	\r 2. Open Garage
    	\r 3. Exit window
    	\r 4. Peek through window
        \r 5. Explore table\n""")
        if (action == '1'):
            rept = False
            shipments()
        elif (action == '2'):
            rept = False
            garage()
        elif (action == '3'):
            print("You have been caught by a guard!")
            print("GAME OVER!!!")
            h = input() #Just to wait for user action before exit
            break #exits the game
        elif(action == '4'):
            print(""" > Sight of a beautiful garden
	              \r > A guard standing right next to the window
	              \r > A fence at the end of the garden """)
        elif(action == '5'):
            if (doorKey == 0): #Check weather player already has keys
                doorKey = 1 #Picks up door key, globally
                print("You have found a door key. This might be useful.")
            else:
                print("You have already explored it.")



#Storage 2 with position value 3
def storage2():
    print("----------------------------------------------------------------")
    global guard1 #Uses global variable to track life of guard
    global smithKey #Uses global variable to track weather player has key
    global hammer
    global position #Uses position as global variable to track player
                    # location
    ##-- Prints a custum message based on player position --##
    if (position == 1):
        print("You have entered storage 2 from garage.")
    elif (position == 4):
        print("You entered storage 2 from shipments.")
    print()
    position = 3

    print(""" > Door on the middle of the eastern wall saying "Garage"
	\r > A door in the middle of the north wall sayng "Shipments"
	\r > A guard on the south western side, next to a table. He
	 appears to be taking a nap.
	\r > A door on the north western wall saying "Main entrance".
	 Probably the guarded main door of the building. """)

    ##-- Prompts the player for actions --#
    rept = True
    while rept:
        print()
        action = input("""What's your action?
          \r 1. Open Garage
    		\r 2. Open Shipments.
    		\r 3. Open main door
    		\r 4. Explore table
    		\r 5. kill guard\n""")
        if (action == '1'):
            rept = False
            garage()
        elif (action == '2'):
            rept = False
            shipments()
        elif (action == '3'):
            print("You have been caught by a guard!")
            print("GAME OVER!!!")
            h = input() #Just to wait for user action before exit
            break #exits the game
        elif (action == '4'):
            if (guard1 == 1): #Checks weather guard is alive
                print("You have been caught by a guard!")
                print("GAME OVER!!!")
                h = input() #Just to wait for user action before exit
                break #exits the game
            else:
                if (smithKey == 0): #Checks for the key
                    smithKey = 1 #Picks up the key
                    print("You found a key. This might be useful.")
                else:
                    print("You have already explored it.")
        elif (action == '5'):
            if (hammer == 1): #Checks wether the player has hammer
                if (guard1 == 1): #Checks wether the guard is alive
                    guard1 = 0
                    print("You killed a guard!")
                else:
                    print("The guard is already dead.")
            else:
                print("You don't have a tool. Get one.")

#Shipments room with position value 4
def shipments():
    print("----------------------------------------------------------------")
    global guard2 #Uses global variable to track life of guard
    global csDoor #Uses to chech wether door is unlocked
    global hammer
    global position #Uses position as global variable to track player
                    # location
    ##-- Prints a custum message based on player position --##
    if (position == 2):
        print("You have entered Shipments from storage 1.")
    elif (position == 3):
        print("You entered Shipments from Storage 2.")
    elif (position == 5):
        print("You entered Shipments from Cold storage.")
    print()
    position = 4

    print(""" > A door on the middle of the southern wall saying
	 "Storage 2"
	\r > A door on the eastern wall, a little towards south saying
	 "Sorage 1"
	\r > A guard on the north eastern corner and he is taking a nap
	\r > A Door on the west wall, towards the north of the room.
	 saying "Cold storage". It appears to be locked.
	\r > A window on the middle of the north wall """)

    ##-- Prompts the player for actions --#
    rept = True
    while rept:
        print()
        action = input("""What's your action?
        \r 1. Open Storage 1
    		\r 2. Open Storage 2
    		\r 3. Open Cold storage
    		\r 4. Exit window
    		\r 5. Peek window
    		\r 6. Kill guard\n""")
        if (action == '1'):
            rept = False
            storage1()
        elif (action == '2'):
            rept = False
            storage2()
        elif (action == '3'):
            if (guard2 == 1): #Checks wether guard is alive
                print("You have been caught by a guard!")
                print("GAME OVER!!!")
                h = input() #Just to wait for user action before exit
                break #exits the game
            else:
                if (csDoor == 0): #Checks wether the door is open
                    print("The door sems to be locked!")
                    unlock = input("Unlock now? y or n: ")
                    if (unlock == 'Y' or unlock == 'y'):
                        if (doorKey == 1): #Checks wether player has the key
                            print("Unlocked")
                            rept = False
                            csDoor = 1 #Opens the door
                            coldStorage()
                        else:
                            print("You don't have the key! Find it.")
                            continue
                    else:
                        continue
                else:
                    rept =False
                    coldStorage()
        elif (action == '4'):
            print("You have been caught by a guard!")
            print("GAME OVER!!!")
            h = input() #Just to wait for user action before exit
            break #exits the game
        elif (action == '5'):
            print(""" > Sight of a garden
	           \r > A guard right next to the window
	           \r > A fence at the end of the garden. """)
        elif (action == '6'):
            if (hammer == 1): #Checks wether the player has hammer
                if (guard2 == 1): #Checks wether the guard is alive
                    guard2 = 0
                    print("You killed a guard!")
                else:
                    print("The guard is already dead")
            else:
                print("You don't have the tool. Get one.")


#Cold storage room with position value 5
def coldStorage():
    print("----------------------------------------------------------------")
    global smithKey #Track the key to unlock Mr.smith
    global smith #track Mr.Smith
    global position #Uses position as global variable to track player
                    # location

    ##-- Prints a custum message based on player position --##
    print("You entered Cold storage from Shipments.")
    print()
    position = 5

    print(""" > Room appears to be deserted.
	\r > On the South western corner Mr.Smith is locked up in a
	 chair.
	\r > There is a window on the middle of the North wall.
	\r > There is a window on the middle of the west wall.""")

    ##-- Prompts the player for actions --#
    rept = True
    while rept:
        print()
        action = input("""What's your action?
         \r 1. Save Mr.Smith
    		\r 2. Peek west window
    		\r 3. peek north window
    		\r 4. Exit north window
    		\r 5. Exit west window\n""")
        if (action == '1'):
            if (smithKey == 1): #Checks wether the player has the key
                smith = 1
                print("Mr.Smith is saved. Now find an exit.")
            else:
                print("He is locked up. Get a key")
        elif (action == '2'):
            print(""" > Sight of a plain area
	              \r > A broken fence at the far end of the plain
	              \r > Appears to be unguarded """)
        elif (action == '3'):
            print(""" > Sight of the garden
	              \r > A fence at the far end of the garden
	              \r > A guard standing right next to the window """)
        elif (action == '4'):
            print("You have been caught by a guard")
            print("GAME OVER!!!")
            h = input() #Just to wait for user action before exit
            break #Exits the game
        elif (action == '5'):
            if (smith == 1): #Checks wether Mr.Smith is saved
                print("Congragulations, Agent.")
                print("You have completed your mission.")
                h = input() #Just to wait for user action before exit
                break #Exits the game
            else:
                print("You are trying to leave without Mr.Smith!")
                sure = input("Are you sure to leave? y or n: ")
                if (sure == 'y' or sure == 'Y'):
                    print("You abandoned Mr.Smith.")
                    print("GAME OVER!!!")
                    h = input() #Just to wait for user action before exit
                    break #Exits the game
                else:
                    coldStorage()







main()
