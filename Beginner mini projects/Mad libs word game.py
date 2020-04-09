'''*************************************************************************************************
NAME: Mad libs word game
DISCRIPTION: A begenner python project that create a story out of user given words
CREATED BY: Thejus S
DATE OF CREATION: 08 Apr 2020
MODIFIED: -
*************************************************************************************************'''
#Function for a story
def beKind():
    print()
    print("Fill The Fields With Random Words")
    n1 = input("Noun: ")
    np1 = input("Noun(Plural): ")
    n2 = input("Noun: ")
    np2 = input("Noun(Plural): ")
    p = input("Place: ")
    ad = input("Adjective: ")
    n3 = input("Noun: ")
    print()

    #------------------------------------------------------------------#
    # You may find a wierd format for the print statement--------------#
    # The 'triple quotes' are used for multiline placement of the code-#
    # to make it look good. And the '\r' is used to remove unnessesary-#
    # tabs and spaces. Try the code without them and u will understand-#
    # Now the 'f' in the begining is used for 'format'. Only then it---#
    # will relpace the variables in their place holder({})-------------#
    #------------------------------------------------------------------#
    print(f""" Be kind to your {n1}-footed {np1}
              \r For a duck may be somebody`s {n2},
              \r Be kind to your {np2} in {p}
              \r Where the weather is always {ad}.
              \r You may think that this is the {n3},
              \r Well it is.""")


#Function for a story
def romeoAndJuliet():
    print()
    print("Fill The Fields With Random Words")
    np1 = input("Noun(Plural): ")
    n1 = input("Noun: ")
    np2 = input("Noun(Plural): ")
    n2 = input("Noun: ")
    ad1 = input("Adjective: ")
    v1 = input("Verb: ")
    num = input("Number: ")
    ad2 = input("Adjective: ")
    bp = input("BodyPart: ")
    v2 = input("Verb: ")
    print()

    #------------------------------------------------------------------#
    # You may find a wierd format for the print statement--------------#
    # The 'triple quotes' are used for multiline placement of the code-#
    # to make it look good. And the '\r' is used to remove unnessesary-#
    # tabs and spaces. Try the code without them and u will understand-#
    # Now the 'f' in the begining is used for 'format'. Only then it---#
    # will relpace the variables in their place holder({})-------------#
    #------------------------------------------------------------------#
    print(f""" Two {np1}, both alike in dignity,
            \r In fair Place, where we lay our scene,
            \r From ancient {n1} break to new mutiny,
            \r Where civil blood makes civil hands unclean.
            \r From forth the fatal loins of these two foes
            \r A pair of star-cross`d {np2} take their life;
            \r Whole misadventured piteous overthrows
            \r Do with their {n2} bury their parents` strife.
            \r The fearful passage of their {ad1} love,
            \r And the continuance of their parents` rage,
            \r Which, but their children`s end, nought could {v1},
            \r Is now the {num} hours` traffic of our stage;
            \r The which if you with {ad2} {bp} attend,
            \r What here shall {v2}, our toil shall strive to mend.""")




def main():
    print("This is a word game where we generate a story with words you enter.")
    print("--------------------------------------------------------------------")
    print("So make your choise:")
    #Story selection part with if-else
    choise = input("1.Be kind   2.Romeo and juliet prologue:  1 or 2: ")
    if (choise == '1'):
        beKind()
    elif(choise == '2'):
        romeoAndJuliet()
    else:
        Print("I said, 1 or 2...")





main()
