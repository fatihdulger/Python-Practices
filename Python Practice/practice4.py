"""Task1: 
Write a countdown timer program
•	That will countdown from 60 
•	 Decrease the count by 1 every time
•	Print the count  """

"""num1 = int(input("Enter a number for multiplication table: "))
# start and stop values
for num2 in range(1,13):
    # num1  multiply by num2
    print(f"{num1} x {num2} = {num1 * num2} ") """

number = range(60,0,-1) # range (start, stop, step value)
for n in number:
    print(n)



"""
Task2:
Research casting in python programming
https://www.w3schools.com/python/python_casting.asp
Use the required constructor function to construct 
Float to integer 
•	23.4
•	1.6
•	2.8
Integer to float
•	1234
•	2
•	67 """
# Casting is specifying types of variables. int(), float(), str()

x= int(23.4)
print(x)
y = int(1.6)
print(y)
z= int(2.8)
print(z)
print(int(5.19))

print(float(1234))
print(float(2))
print(float(67))
print(float("3.9"))


"""
Task3 
Write a pseudocode for the multiplication table program below
-Pseudocode is informal steps for an algorithm using structured English. 
There is no specific syntax for pseudocode, and it should be human readable so that a programmer can translate it into program code. 
-Pseudocode is used to design programs
-It is intended for humans to read and not for a computer to interpret. 

 """
 
"""num = int(input)"enter a number to generate multiplication table: ")) # prompt for user input
 for multiplyby in range(1,13): # loop from start to end value/range
    print(num, "X", multiplyby, "=", num * multiplyby ) # returnt the looped result
"""

num = int(input("Enter a number to generate multiplication table: ")) # prompt for user input
for multiplyby in range(1,13): # loop from start to end value/range
    print(num, "X", multiplyby, "=", num * multiplyby)



"""
Task4:
1- What is the difference between While Loop and For Loop; explain with screenshot of your program
Basically; Use a for loop when the number of iteration is known(how many times you want to do something for).

a) While Loop:
The initialization and the condition checking is done at the beginning of the loop.
It is used only when the number of iterations isn’t known.
If the condition is not mentioned in the 'while' loop, it results in a compilation error.
If the initialization is done when the condition is being checked, then initialization occurs every time the loop is iterated through.
The iteration statement can be written within any point inside the loop.

userGuess = input("Enter your guess word: ").title()
guessWord = "Cohort10"

while userGuess != guessWord:
    userGuess = input("Incorrect, guess again!").title()
print(f"You guessed {userGuess} is correct")

# exp 2:num = 2 # int(input("enter a number: "))
"num = 2 is the start value"

while num <= 20: # set the condition to check the numbr will increment until it gets to 20
    print(num)
    num += 1   # it will inrement starting from 2 until 20
    
    if num == 15:  # set the Condition that if true will exeute the break syntax below

        print("condition met")

        break  # break out of the loop

    num += 1
    

b) For Loop:
The initialization, condition checking, and the iteration statements are written at the beginning of the loop.
It is used only when the number of iterations is known beforehand.
If the condition is not mentioned in the 'for' loop, then the loop iterates infinite number of times.
The initialization is done only once, and it is never repeated.
The iteration statement is written at the beginning.
Hence, it executes once all statements in loop have been executed.
exp:
 for findNum in range(5,10): # specify the start and stop value

    time.sleep(2)
    print("Using start and stop\n")


2- Why is data validation important when user input is required?  
>> Data validation is essential part when handling data. 
>>if data  isn't accurate from start our results will not be accurate either. it is very important
>> we have to get the user data in the form we want or can handle then design an interaction with user to give us what we want
>> or make casting to gather information in the form we can use.

name = input("Enter your name: ")
if name.islower(): # check if user input is lower case
    print(f"Welcome {name}")
else:
    print(f"Your {name} is not in lower case")
    exit()

3- Explain casting in python programming """

# it is changing data type after user input asked. integer to float or string ? 
