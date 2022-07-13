from random import shuffle

mySuits = ["♥ ", "♦", "♣", "♠"]
myDeck = []  # empty list

for item in mySuits:
    for card in range(1, 14):  # start value is 1 end value is 14
        if card == 11:
            # change/replace the value of 11 and add it the myDeck list with values ["♥ ","♦", "♣", "♠"]
            myDeck.append("J" + item)
        elif card == 12:
            myDeck.append("Q" + item)
        elif card == 13:
            myDeck.append("K" + item)
        elif card == 1:
            myDeck.append("A" + item)
        else:
            myDeck.append(str(card) + item)
print(f"Unshuffled deck of cards\n {myDeck}")
shuffle(myDeck)
print(f"Shuffled deck of cards\n {myDeck}")
