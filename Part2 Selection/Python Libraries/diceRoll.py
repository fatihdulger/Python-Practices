import random

"player 1"

die1 = random.randint(1,6)
die2 = random.randint(1,6)

print(f"Die 1 = {die1}\nDie 2 = {die2}")

dice = die1 + die2 # value from first die added to second die
print(f"Dice value: {dice}")
if dice == 12:
    dice = 0
    print("Disqualified")
else:
    if die1 == die2:
        dice = dice * 2
player1Score = dice
print(f"Player1 score {player1Score}")

"player 2"

die3 = random.randint(1,6)
die4 = random.randint(1,6)

print(f"Die 3 = {die3}\nDie 4 = {die4}")

dice1 = die3 + die4 # value from first die added to second die
print(f"Dice value: {dice1}")
if dice1 == 12:
    dice1 = 0
    print("Disqualified")
else:
    if die3 == die4:
        dice1 = dice1 * 2
player2Score = dice1
print(f"Player2 score {player2Score}")

# comparison

if player1Score > player2Score:
    print(f"player 1 is winner with score {player1Score}")
elif player2Score > player1Score:
    print(f"player 2 is winner with score {player2Score}")
else:
    print(f"Game is tie-breaker with equal scores of {player1Score}, {player2Score}") 

