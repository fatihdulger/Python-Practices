# create a dictionary
" name  {key: value, key: value, key: value, key:value} "

# create a dictionary

"  name     { key: value,   key: value,   key: value,   key: value,  key: value  } "

dict2 = {1: "Anna", 2: "Lucy", 3: "Alice", 4: "Chloe"}

print(dict2)



userDetails = {"fName": "", "course": "", "module": ""}

# use the input function to capture user data

userDetails["fName"] = input ("Enter your Fullname: ")
userDetails["course"] = input ("Enter Course: ")
userDetails["module"] = input ("Enter Module: ")

print(userDetails)

# create a dictionary with no keys or values

userDetails1 = {} # create an empty dictionary
userDetails1Key = input("Enter Key: ") # ask for a key
"userDetails1['Age']"
userDetails1[userDetails1Key] = input (f"Enter value for {[userDetails1Key]}")  ## 
print(userDetails1)

##############
userDetails1 = {}  # create an empty dictionary check this

userDetails2Key = input("Enter Key: ")  # ask for key

userDetails2[userDetails2Key] = input(f"Enter value for {[userDetails1Key]}")

print(userDetails2)



if userDetails1Key == userDetails2Key:
    print("Same key")


"""playerList = [] # create an empty list
addPlayer = True # Flag variable "addPlayer " is of Boolean dataType

while addPlayer:  # while True execute the code below
    # ask for user input respectively
    pName = input("Enter Player name: ")
    pPass = input("Enter Player pass: ")
    pScore = int(input("Enter Current Score: "))
    pHscore = int(input("Enter High Score: "))

    playerProfile = {
        "playerTag" : pName,
        "pass": pPass,
        "currentScore": pScore,
        "highScore": pHscore

    }

# add player profile to player list
    playersList.append(playerProfile)
    anotherPlayer = input("Do you want to add another player? Y/N ").upper()
    if anotherPlayer == "N": # check/compare user response with the string value N
        addPlayer = False  # reset the flag variable to False to break out of the while loop.

print(f"the list of players are\n{playersList}") """

