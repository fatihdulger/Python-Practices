# declare list c10 assign values to it



#          0         1          2       3         4         5       6

lstC10 = [
    "Ole",
    "Michelle",
    "Adam",
    "Fatih",
    "Danielle",
    "Ola",
    "Adam",
]
lstModules1 = []
lstModules2 = ["HTML", "CSS"]
print(lstModules2)
# use the insert method to insert an item in a list specified by the index posion
# 0 1  2  3 4  5  6   7 8....
"       index position, item                "
lstModules2.insert(0,"SDLC")
print(lstModules2)

lstModules2.insert(3, "JS")
print(lstModules2)

#append an item to a list

lstModules2.append("MySQL")
lstModules2.append("NoSQL")
lstModules2.append("Python")
print(lstModules2)
print(lstModules2[2]) # access items in a list by index position

print(f"The length of the list is: {len(lstModules2)}") # return the length of the list

# delete an item form a list
del(lstModules2[3]) # delete item by index position
print(lstModules2)

# delte/remove an item from a list by value
lstModules2.remove("SDLC")
print(lstModules2)

# sort list items

lstScores = [10, 12, -1, 23,45,12,78]
lstScores.sort(reverse=True)
print(f"Sorted in ascending order: {lstScores}")
lstScores.clear()
print(f"Cleared list {lstScores}")

# Slicing items

print("Slicing list items")
" 0   1   2   3   4   5   6   7  "
print("Slicing list items")

"0           1       2     3      4        5         6  "

"['SDLC', 'HTML', 'CSS', 'JS', 'MySQL', 'NoSQL', 'Python']"
print(lstModules2[2:5])  # index position of items
print(lstModules2[1:5])
print("End of slice")