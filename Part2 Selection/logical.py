# Logical expression evaluste to true or false
"Logical operators: and, or, not"

#Comparison operator compare values
# """Comparison operator compare values
# ==    equal  ( 2 == 2)
# <   less than
# >   more than
# <=  less than or equal to
# >=  greater than or equal to
# !=    Not equal to """

num1 = 10
num2 = 5

print(num1 == num2)
print(num1 == 10)
print(num2 == 5)

# and, or, not "

print("the and operator")
print(num1 == 10 and num2 == 5) # true
print(num1 == 10 and num2 == 50) # false

print("the or operator")
print(num1 == 10 or num2 == 5)  # true becuase it is OR opeator
print(num1 == 10 or num2 == 50) # true it looks for 1 of them to be true
print(num1 == 20 or num2 == 50) # false

print("the not operator") # negating

print(not(num1 == 10))
print(not(num1 == 10 and num2 == 5))
print(not(num1 == 10 and num2 == 50)) # true 

print("the not with or operator") # negating

print(not(num1 == 10 or num2 == 5))
#print(not(num1 == 10 and num2 == 50))


print(not (num1 == 10 or num2 == 5))  # num1 is not equal to 10 and num2 isnot equal to 5

print(not (num1 == 10 or num2 == 50))