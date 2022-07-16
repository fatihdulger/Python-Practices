num = int(input("Please enter a number: "))
if num > 10:
    print('The number is too high')
else:
    print("Thank you")

import random

randNums1 = random.randint(1,6)
print("The random number is ", randNums1)

import math
radius = float(input("Enter radius: "))
#invoke the math.pi method from the math library
area = math.pi * radius **2
print("The area is: ", area)

for findNum in range(5,56, 10): # specifying start stop step value
    print(findNum)

num1 = int(input("Enter a number for multiplication table: "))
# start and stop values
for num2 in range(1,13):
    # num1  multiply by num2
    print(f"{num1} x {num2} = {num1 * num2} ")