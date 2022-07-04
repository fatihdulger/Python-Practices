# nested Selection is when a selectin block(if/else) is placed within another selection block

userAge = int(input("Enter your age: "))
ageLimit = 16
passCode = "Cohort10"
if userAge > ageLimit: # compare the value enter in userAge variable with the value held in agelimit
    userCode = input("Enter code: ") # executed if userAge is greater thatn the value held in ageLimit
    if userCode == passCode: # this if block is nested.
        print(f"Your code {userCode} is valid. Access granted!")

print("closing")
