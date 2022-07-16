num = int(input("enter a number to generate multiplication table: ")) # prompt for user input
for multiplyby in range(1,13): # loop from start to end value/range
    print(num, "X", multiplyby, "=", num * multiplyby)





list1 = [1,5,9,10,7.3, "listA", "listB"]
print(type(list1))

tuple1 = (6,4,8,9, -4, "my tuple")
print(tuple1)
print(type(tuple1))

set1 = {4,5,6,8,10,31,2.4,"abd", "uk"}
print("\nThis is a set")
print(type(set1))
print(set1)

dictionary1 = {1:"Fatih", 2:"Mualla", 3:"Ahmed Melih", 4:"Beyza Elif"}
print("\nThis is a dictionary")
print(type(dictionary1))
print(dictionary1)