"""Use a for loop when the number of iteration is known(how many times you want to do something for).

A for loop also controls the flow of execution a program."""

# iteration means to repeat

import time

"syntax "
# for variableName in range method (number of iteration)

for findNum in range(10):# specify number of iteration to be 10


    print(findNum)

time.sleep(2)
print("Using start and stop\n")

for findNum in range(5,10): # specify the start and stop value

    time.sleep(2)
    print("Using start and stop\n")

for findNum in range(5,56, 10): # specifying start stop step value
    print(findNum)

# modify any of the code above to create a countdown

    time.sleep(2)
    print("USing start, stop and step\n")
