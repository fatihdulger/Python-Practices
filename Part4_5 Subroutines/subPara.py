# keyword name (parameter1, parameter2)

def addition(paraNum1, paraNum2):    # parameters are passed inside the braces of the subroutine
    total = paraNum1 + paraNum2
    print(f"Your answer is to {paraNum1} + {paraNum2} = {total}")


# method 1

print("first subroutine call")

addition(21,10) # passed hardcoded values as argument


# method 2

print("Second subroutine call")

argNum1 = int(input("Enter a number: "))

argNum2 = int(input("Enter second number: "))



addition(argNum1, argNum2 ) # passed in the respective variables as arguments

# method 3

print("Third subroutine call")

# passed in the input function asking for the respective values as arguments

addition(int(input("Enter a number: ")), int(input("Enter second number: ")))





#Method 4

print(f"Your username is {parUname}")

username("Jane")

argUser = input("Enter your username: ")

username(argUser)

username(input("Enter your username: "))


def username(): # define a subroutine called username
    uName = input("enter your username: ")
    print(f"Your username is {uName}")
