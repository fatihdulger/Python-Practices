"""
As a programmer your program needs to cater for all inputs.
Therefore, you neeed to ensure checks to handle unexpected data data entry"""

#Try and except is for handling error and validation in python

"""print(name)
name = "Jane"   ## this error will crash the program so we need to deal with this.

print("Today is Thursday") """

try:  # will attempt to run the code in the TRY block
    print(name)

except NameError:
    print("The variable does not exist")


name = "Jane"   
print("Today is Thursday")
print(name)


