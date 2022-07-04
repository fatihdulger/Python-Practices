# nested Selection is when a selectin block(if/else) is placed within another selection block

userAge = int(input("Enter your age: "))
ageLimit = 16
passCode = "Cohort10"
if userAge > ageLimit: # compare the value enter in userAge variable with the value held in agelimit
    userCode = input("Enter code: ").title()  # executed if userAge is greater thatn the value held in ageLimit - title() is for making first letter upper case
    if userCode == passCode: # this if block is nested. (child if  this is nested)
        print(f"Your code {userCode} is valid. Access granted!")
    else:
        print(f"Your code {userCode} is invalid. Access Denied!") # this else is for child if parent if still needs else too.

else:
    print(f"You are {userAge} years old and below the age limit!")
    