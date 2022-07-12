# A lambda is simply a way to define a function in Python. They are sometimes known as "lambda 
# operators" or "lambda functions".  A lambda function is a small anonymous function, they are functions
# that don't need to be named. They are used to create small, one-off functions in cases where a "real "
# function would be too big and bulky.   A lambda function can take any number of arguments, but can 
# only have one expression. lambda arguments : expression .

# Lambdas return a function object, which can be assigned to a variable. Lambdas can have any number
#  of arguments, but they can only have one expression. You cannot call other functions inside lambdas.

#USE LAMBDA for small functions or for 1 time use!!!


#"Lamda arguments : expression. "

addNum = lambda num1: num1 + 23
print(addNum(10))

addNum2 = lambda num1, num2: num1 + num2 + 5
print(addNum2(7, 12))

addNum3 = lambda num1, num2: num1 + num2 + 5
argNum2 = int(input("Enter Number: "))
print(addNum2(7, argNum2))

