# The assert is used for code debugging. Use to test a condition
# and will raise an assertion error if the condition fails

myWord = input("Enter a word with min character 5: ")
# the condition, the output if the condition is not met!

assert len(myWord) >= 5, "Minimum 5 Characters required"
print(f"Welldone, requirement met")

nums = int(input("Enter a number between 5 and 50: "))
# the condition, the output if the condition is not met!
assert 50 > nums > 5, "number must be between 5 and 50"
print(f"number {nums} is between 5 and 50")

userGuess = input("Enter username: ")
# the condition, the output if the condition is not met!
assert userGuess == "superman", "Incorrect username"
print(f"Welcome {userGuess}")

## use this for DEBUGGING