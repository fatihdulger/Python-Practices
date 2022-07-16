# Task3 
# Write a program that will ask the user for how many sweets are in the bag.  
# •	It should also ask how many people the sweets should be shared between.  
# •	Use the whole number division to work out how many sweets each person should have and use the remainder division to find out how many sweets would be left remaining.  
# •	For example if there are 14 sweets in the bag and this was to be divided between 3 people then the programme should display “There will be 4 sweets each and there would be 2 left over.”

sweets = int(input("Enter how many sweets in the bag?: "))
people = int(input("How many people "))
left = sweets % people
print(left)
print(f"each person has {int((sweets - left) / people)} sweets. and {left} left in the bag")

# Task4 
# # import random
# from random import randint
# randNums1 = randint(1,6)
# randNums2 = randint(1,6)
# print("The random number is ",randNums1)
# print("The random number is ",randNums2)
# print("\nThe random number are ",randNums1, randNums2)
# Complete the code provided above to use if and else:
# •	To print out if a double is thrown
# •	To print out if a double is not thrown

from random import randint

randNums1 = randint(1,6)
randNums2 = randint(1,6)

print("The random number is ",randNums1)
print("The random number is ",randNums2)
print("\nThe random number are ",randNums1, randNums2)

if randNums1 == randNums2:
    print(f"a double dice has been thrown with {randNums1, randNums2}")
else:
    print(f"double dice hasn't been thrown {randNums1, randNums2}")



# Task5
# Modify your code in task 4:  
# •	To ask for one user input between 1 and 10
# •	Compare the user input with the random generated number
# •	Print out if a double is thrown
# •	Print out if a double is not thrown

randNumsUser = int(input("enter number between 1 to 10 = "))
randNumsRandom = randint(1,10)

if randNumsUser == randNumsRandom:
    print(f" the user has same random number {randNumsUser, randNumsRandom}")

elif randNumsUser > randNumsRandom:
    print(f"The user has greater number of first and second is the machine random {randNumsUser, randNumsRandom}")
else:
    print(f"The user has less number than machine {randNumsUser, randNumsRandom}")




