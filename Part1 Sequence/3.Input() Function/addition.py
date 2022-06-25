# input function: allow the program to take use input
# the default datatype is string

#Method 1

#num1 = input("Enter a your first number: ")
num1 = int(input("Enter a your first number: "))
#num2 = input("Enter a your second number: ")
num2 = int(input("Enter a your second number: "))
sum = num1 + num2  # string
print(type(sum))

print(f"The sum of {num1} + {num2} = {sum}")

# "Method 2"
num3 = input("Enter a your first number: ")

num4 = input("Enter a your second number: ")

answer = int(num3) + int(num4)

print(type(answer))

print(f"The answer of {num3} + {num4} = {answer}")



# Exercise2: use the print statement to print in new line

# Your name

# Your address

# Your interests

"Modify the eexercise above to ask for input instead of hardcoded values"

"print out the values inpuuted"

fullName = input("Enter your full name please: ")
address = input("please enter your address: ")
interests = input("please enter your hobbies: ")
yourDetails= fullName + address + interests
print(f"The details of you are {fullName} + {address} + {interests} = {yourDetails}")
