# Data types are nothing but variables you use to reserve some space in memory.
# Python variables do not need an explicit declaration to reserve memory space.
# The declaration happens automatically when you initialised a value to a variable.

"string datatype"
username = "c10user1" # implicit datatype because the value is wrapped in quotes
userName = "c10user2"
string1 = """
multiline
multiline
multiline  
"""
string2 = ""
string3 = "Lucy Smith"

print(type(username))
print(type(userName))
print(type(string1))
print(type(string2))
print(type(string3))


# Boolean datatype: True/False
boolVal1 = True
boolVal2 = False
print(type(boolVal1))
print(type(boolVal2))

# numeric data types

num1 = 12  # int datatype

num2 = 13.6  # float datatype

print(type(num1))
print(type(num2))