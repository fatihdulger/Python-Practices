 
#With the filter function, the process is much the same.

# Filter takes a function and applies it to every element in a list

# and created a new list with only the elements that caused the function to return True.

c10People = ["Hanna", "Lucy", "Jane", "Anna", "Lucian", "Amy", "Janet"]
search = input("Enter name: ") # anna
foundP = list(filter(lambda listitem: listitem == search, c10People))
print(f"Found the user {foundP}")  # if found Found the user ['Anna'] will come


userNums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # list

print(f"Original numbers are: {userNums}")

filteredNums = list(filter(lambda evenNums: evenNums % 2 == 0, userNums))  ## so list doesnt only take parameters it also can access to lambda and operations 
print(f"Filtered numbers are: {filteredNums}")

filteredNums = list(filter(lambda evenNums: evenNums % 3 == 0, userNums))  ## we just changed the modulus remaining 
print(f"Filtered numbers are: {filteredNums}")