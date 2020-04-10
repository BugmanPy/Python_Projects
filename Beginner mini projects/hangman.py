'''*************************************************************************
NAME: Hangman
DISCRIPTION: A begenner python project that create a basic hangman game.
CREATED BY: Thejus S
DATE OF CREATION: 09 Apr 2020
CONTRIBUTORS: Max Abraham James, Sangeeth AK
MODIFIED: 10 Apr 2020
*************************************************************************'''
import random

def main():
    ##-- List of words --##
    wordList = ["adapt","sugar","honey","poetry","onion"]

    ##-- Main Loop --##
    rept = True
    while rept:
        id = random.randint(0,4)
        word = wordList[id] #Picks a random word from the list
        letterList = list(word) #Creates a list of letters
        l = len(letterList)-1 #length of list - 1

        x = random.randint(0,l) #A numner to pick a random letter
        check = True
        while check:
            y = random.randint(0,l) #Second num for random letter
            if (y != x): #Both x and y must not be same
                break
            else:
                continue

        printList = [0] #Creates a list for printing the word
        printList.pop(0)
        for i in range(l+1):
            if (i == x):
                ## Adding the xth position letter of the word to the xth
                ## position in the printList
                printList.insert(i,letterList[i])
            elif (i == y):
                ## Adding the yth position letter of the word to the yth
                ## position in the printList
                printList.insert(i,letterList[i])
            else:
                ## if i not equal to x or y, fill it with dashes
                printList.insert(i,"_")
        ##-- Now the printList will be identical to the letterList with
        ##-- two letters in the same spot and rest with dashes

        life = 3 #Sets the life value to cout number of chances
        ##-- Loops as long as the player has life --##
        gameLoop = True
        while gameLoop:
            print("--------------------------------------")
            save = 0 #Variable to track the succesful input of a player

            ##-- Life display section --##
            print("Life: ",end=" ")
            for j in range(life):
                print("-<3- ",end=" ")
            ##------------------------##
            print()
            print()
            #print(printList) #Printing the word list with dashes
            print(" ",end=" ")
            for p in printList:
                print(p,end=" ")

            # User inputs a charector
            userLetter = input("\n\nEnter a missing letter: ")

            ##-- Checks wether the charector is in the original word --##
            for k in range(l+1):
                #print("loop "+str(k)) #Debugging
                #print(userLetter+"  "+letterList[k]) #Debugging
                if (userLetter == letterList[k]):
                    #print("user = letter. Checking print") #Debugging
                    #print(printList[k]) #Debugging
                    ##-- If the kth position in the list is a dash, replace
                    #    it with the user entered letter               --##
                    if (printList[k] == '_'):
                        #print("print is _") #Debugging
                        printList.pop(k) #Removes the alredy present dash
                        printList.insert(k,userLetter)
                        save =1
                        break
                    else:
                        continue

                    break
                else:
                    continue
            ##-- Checks wether the whole word is completed --##
            if (printList == letterList):
                print(">>> Word Completed. Good job")
                print("Word: ",end=" ")
                #Printing the word list
                print(" ",end=" ")
                for p in printList:
                    print(p,end=" ")
                break

            ##-- If player enters a wrong letter, take away 1 life --##
            if (save == 0):
                life = life -1
                print(">>> Wrong letter. Lost a life!")
                ##-- Checks wether the life count is zero --##
                if (life == 0):
                    print(">>> You have lost all life. GAME OVER!")
                    break
            else:
                continue


        ##-- Repeating the game. Affects the main loop, not the gameLoop--##
        print()
        print()
        again = input("Go again? y or n: ")
        if (again == 'y' or again == 'Y'):
            rept = True
        else:
            rept = False







main()
