'''*************************************************************************************************
NAME: Dice roll simulator
DISCRIPTION: A begenner python project that aims to simulate the roll of a die
CREATED BY: Thejus S
DATE OF CREATION: 08 Apr 2020
MODIFIED: -
*************************************************************************************************'''

import random # Creation of random number of dice rolls requires this module

def main():
    print("Starting.....")
    print()
    #--- Logic ----#
    uin = True
    while (uin==True):
        print()
        randInt = random.randint(1,6) # Generates a random number between 1 and 6
        print("The number is :",end=" ")
        print(randInt)
        again = input("Roll again? y or n: ")
        if (again == 'y' or again == 'Y'): #Changes the while loop condition
            uin = True
        else:
            print("Stopping...")
            uin = False
    #---------------#


main()
