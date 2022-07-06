
# While loop: keeps looping until a condition is met

# While loop: keeps looping until a condition is met    userGuess = input("Enter your guess word")guessWord = "Cohort10"while userGuess != guessWord:    userGuess = input("Incorrect, guess again!")print(f"You guessed {userGuess} is correct")

userGuess = input("Enter your guess word: ").title()

guessWord = "Cohort10"



while userGuess != guessWord:

    userGuess = input("Incorrect, guess again!").title()

print(f"You guessed {userGuess} is correct")