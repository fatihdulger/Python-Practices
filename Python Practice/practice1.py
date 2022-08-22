#Homework Practice 1
# Create the following python programs using the knowledge gained from today’s session: 
# 1.	Write a program that will ask the user for their first name and then their surname and then will display their full name.
# 2.	Write a program that asks for 3 numbers (num1, num2 and num3).  Display the output where it adds together num1 and num2 and then multiplies this total by num3. Input intnum
# 3.	Ask the width, length and depth of a swimming pool and then work out the amount of water that the swimming pool will hold in cubic meters.
# 4.	Ask the user to input the number of hours a worker has worked in a week. Ask the user to also enter the amount that worker earns per hour. Work out the total pay the worker should get for the week’s work.
# Note: it is important you follow the variable naming convention discussed in today’s session and use the input function to capture user input instead of hardcoded static value assignment for variables.

#Answer 1

name = input("Enter a your first name: ")
surname = input("Enter a your surname: ")

fullName = "name " + surname
fullName = name + " " + surname

print(f"My name is {fullName}")
print(f"My name is {name} {surname}")

# Answer 2 

num1 = int(input("Please enter your 1st number: "))
num2 = int(input("Please enter your 2nd number: "))
num3 = int(input("Please enter your 3rd number: "))
numCalc= (num1 + num2) * num3

print(f"the calculation for your numbers is: {num1} + {num2} * {num3} = {numCalc}")

# 3 Answer

width = float(input("please enter your swimming pool's width in meters here: "))
length = float(input("please enter your swimming pool's length by meter here: "))
depth = float(input("please enter your swimming pool's depth by meter here: "))

totalVol = width * length * depth

print(f"based on your pool's measurement entered, the amount of water to fill the pool is: {totalVol} m3")



# 4 Answer

workHours = int(input("Enter working hours in a week: "))
rateHour = int(input("Enter hourly rate: "))

print(f"totalpay: {workHours}x{rateHour}", workHours*rateHour)

workHours = int(input("Enter working hours in a week: "))
rateHour = int(input("Enter rate per hour: "))

print(f"totalpay: {workHours}x{rateHour} =", workHours*rateHour)