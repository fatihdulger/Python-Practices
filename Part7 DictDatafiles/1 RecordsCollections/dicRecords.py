""" A record is a static data structure. You must determine the attributes and the data
types for each entity # during declaration. These will then be fixed for each record
used in the database. 
# Python does not have # a native data structure for a record.
data structure called a dictionary to represent a record.  A # dictionary has some of
the features of a record. 
# A dictionary has key value pairs and is mutable in nature. """

# Create dictionary
dict1 = {1: "Jenny"} # is a record in a dictionary
dict2 = {1: "Anna",2: "Lucy",3: "Alice",4: "Chloe"} # a dictionary with 4 records

print(dict1)
print(dict2)
print(dict2[3]) # print a secific value in a record based on the key
print(dict2.items()) # use the items method to print all records

courses = {"course1": "SDLC", "course2": "HTML", "course3": "CSS", "course4": "JS", "course5": "DB"}

# print using the keys method

dkeys = courses.keys() # access all the keys in the dictionary !!!
print(f"List of keys {dkeys}")

for aKey in dkeys:
    #aKey = course1...course2.....
    print(aKey)


# Exercise modify the code above to use the values() to print only the values


dValues = courses.values() # access all the keys in the dictionary !!!
print(f"List of keys {dValues}")

for aVal in dkeys:
    #aKey = course1...course2.....
    print(aVal)
    

