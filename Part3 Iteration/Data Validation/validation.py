name = input("Enter your name: ")

if name.islower(): # check if user input is lower case
    print(f"Welcome {name}")
else:
    print(f"Your {name} is not in lower case")
    exit()