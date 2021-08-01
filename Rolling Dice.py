from random import *



def rollDie():
    numFaces = int(input("How many sides does this die have?"))
    numResult = randint(1,numFaces)

    print(numResult)

    retry = input("Would you like to try again? (Y/N)").upper()

    if retry == "Y":
        rollDie()
    else:
        exit()

rollDie()