playerList = [] # create an empty list
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

print(f"the list of players are\n{playersList}")