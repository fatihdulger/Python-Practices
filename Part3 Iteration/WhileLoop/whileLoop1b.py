


userGuess = input("Enter your guess word: ").title() # first attempt

guessWord = "Cohort10"

guessAttempts = 1 # flag variable value = 1

while userGuess != guessWord and guessAttempts <3:
    # ask the user to gess again and again ... until the condition is met / 
    userGuess = input(f"You have used {guessAttempts}/3 attempts!\nTry again: ").title()
    guessAttempts +=1
#print(f"You guessed {userGuess} is correct")

if userGuess == guessWord:
    print(f"You have guess {userGuess}")
else:
    print(f"You have used {guessAttempts}/3 attempts!")

# if you copy while condition here below it will still work 

# while userGuess != guessWord and guessAttempts <3:
#     # ask the user to guess again and again ... until the condition is met / 
#     userGuess = input(f"You have used {guessAttempts}/3 attempts!\nTry again: ").title()
#     guessAttempts +=1