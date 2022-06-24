# A variable holds a value in memory location that is needed for the
# of the program
# A variable can can hold one value at a time. This value can change throughout the
# execution of the program and must be declared before it is used.

"Variable declaration and assingment"

num1 = 10 # Datatype in python is implicit: num1 is assigned an integer data because of the value 10

print(type(num1)) # returns the data type of the variable

print("num1 data type is of ", type(num1))

num2 = 30

print(f"The answer to {num1} + {num2} = {num1 + num2}")
print(f"The answer to {num1} x {num2} = {num1 * num2}")

fullName = "John Smith"
print(f"Hello {fullName}")
print("Hello ",fullName, "you are", num2, "years old")
print(f"Hello {fullName} you are {num2} years old")
# casting is converting from ne datatype to another/different datatype
print("Hello " + fullName +  " you are " + str(num2) + " years old")
# concatenate means to join

fullName = "Jane Doe" # the variable fullName has been re-assigned 
print("Hello " + fullName +  " you are " + str(num2) + " years old")

num2 = 50 # the variable num2 has been re-assigned a different value 50
total = num1 + num2
print(f"The total is {total}")
# variable naming convention

username = "c10user1" # use meaningful name
userName = "c10user2" # use camelCase notation
user_name = "c10user3" # use snake case / underscore between two words
username4= "c10user4" # use meaningful name
firstName = 'Lucy Smith' # single quotes use for string values
userAge = 23

#DO NOT  DO this
AGE = 12 # unless it is a constant
# £cash or $cash = 12 # dont use symbols

User = "c10user5" # no caps at start of variable name
# user name = "anna" # no space/s between words/variable name
#1user = "jam1" dont start a variable name with a number

print("The value of initial age is ", AGE)

AGE = 13 
print("The value of age is now ", AGE)

