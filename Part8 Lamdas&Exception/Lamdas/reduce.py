# Reduce is another cool Python function. It applies a rolling calculation to all items in a list. 
# You could use this to tally up a sum total, or multiply all numbers together:
# If you're doing anything more than a basic task, or want to call other methods, use a normal function. Lambdas are great for one off, anonymous functions, but they must only have a single expression. 

from functools import reduce

userNums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"num1 + num2 =ans, num1(ans) + num2 = ans"
# 1+2 = 3, 3+3 = 6, 6 +4 = 10

print(f"Original numbers are: {userNums}")

rolledNums = reduce(lambda num1, num2: num1 + num2, userNums)
print(f"Apllied rolling calculation: {rolledNums}")