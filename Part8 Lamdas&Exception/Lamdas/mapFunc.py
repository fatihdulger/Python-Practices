# The map function expects two arguments: a function and a list. 
# It takes that function and applies it to every element in the list, 
# returning the list of modified elements as a map object. 
# The list function is used to convert the resulting map object back into a list again.

userNums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
multiplyN = 5 # int(input("Enter number: "))
result = list(map(lambda num: num * multiplyN, userNums))  ## userName should be there second to multiplyN to provide for "num" - like placeholder - because there is no num provided other than the list
print(result)

#userNums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
multiplyN = 5 # int(input("Enter number: "))
result = list(map(lambda num: num * 11, [20, 20, 40, 50, 60]))  ## good explanation of above program
print(result)


