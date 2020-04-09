'''*************************************************************************************************
NAME: Guess the number
DISCRIPTION: A begenner python project that lets user to guess the number picked by the programme
CREATED BY: Thejus S
DATE OF CREATION: 08 Apr 2020
MODIFIED: -
*************************************************************************************************'''
import random #Require this module to generate random number

def main():
    print("This is a number guess game.")
    print("I will think of a number (1 to 5) and you will have to guess it.Good luck.")
    print("---------------------------------------------------------------------------")
    begin=input("shall we begin? y or n: ")
    print()
    print()
    #------- Logic ---------#
    if (begin == 'y' or begin == 'Y'):
        again = True #While loop condition
        score = 0 #Score value
        while again:
            myNum = random.randint(1,5) #The number guessing part
            print("I Choose...")
            yourNum = int(input("Your guess? : ")) #User input part
            print()
            # Compares user input with guessed number
            if (myNum == yourNum):
                print("Congragulations, You guessed it right.")
                score = score+1
            else:
                print("Oops, wrong guess..")

            agn = input("Wanna try again? y or n: ")
            print()
            #Changes the while loop condition
            if (agn == 'y' or agn == 'Y'):
                again = True
            else:
                again = False

        print("Your total score is "+str(score)) #Prints the Score
        print("thanks for playing.")
    else:
        print("ok...")

    #----------------------------#







main()
