from mysqlConnect import *
import readMembers
import addMembers
import deleteMembers
import updateMember
import searchMembers
import time


def menuOptions():
    options = 0 # flag variable optioons = 0
#check if the value held in flag variable is a match with the list of items
    while options not in ["1", "2", "3", "4", "5", "6"]:
        print("Songs Menu Options:\nEnter \n1. To Print.\n2. To Add.\n3. To Update.\n4. To Delete.\n5. To Search\n6. To Exit")
    # re-assign the options variable with a different value
        options = input("\nEnter one of the options above")
        if options not in ["1", "2", "3", "4", "5", "6"]:
            print(f"{options} is not a valid choice!")

    return options

# menuOptions()   comment out to carry on with boolean

# crate a boolean flag variable and set it to True

mainProgram = True

while mainProgram == True:
    mainMenu = menuOptions() # we assinged the menuOptions function to a variable
    # if mainMenu = 1/2/3/4/5 we can then call the respective app and its subroutine
    if mainMenu == "1":
        readMembers.readMembers()
    elif mainMenu == "2":
        addMembers.addMember()
    elif mainMenu == "3":
        updateMember.updateMembers()
    elif mainMenu == "4":
        deleteMembers.deleteMembers()
    elif mainMenu == "5":
        searchMembers.searchMember()
    else: # re-assign the value held in the mainProgram flag variable to False

        mainProgram = False

    input("press Enter to Exit: ")

