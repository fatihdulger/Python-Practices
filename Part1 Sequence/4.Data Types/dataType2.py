"""
List is an ordered sequence of items. It is a very flexible data type in python
The values in a list doesn't have to be of the same type. Items in a list can be modify
"""

# declare list c10 assign values to it

lstc10 = ["Ole", "Michelle", "Adam", "Fatih", "Daniele", "Monica"]
print(type(lstc10))
lstModules = []
print(type(lstModules))

print(lstc10[3])

"""
Tuple is a sequence of items that are in order
 and it is not possible to modify the tuples. Therefore,
 tuples are faster than list and the primary use of tuples
 is to create write protect data
 items can be accessed based on their index position

"""
# declare tuple and assigned different data type
tpl1 = ("a", "b", "c", 10, 12, -1, 23)
tpl2 = ("mytuple")  # if you put coma it will be tuple ("mytuple",)
print(type(tpl1))
print(type(tpl2))

# SET

set1 = {
    "a",
    "b",
    "c",
     "Fatih",
    "Danielle",
    10,
    12,
    -1,
    23,
    "Ole",
    "Michelle",
    "Adam",
     "b",
    "c",
    "Fatih",
    "Danielle",
    "Ola",
    "Adam",
}
print(type(set1))
print(set1)

# DICTIONARY

"Dictionary store data as key value pairs"

dictionary1 = {1: "Tysion", 2: "Georgio", "name": "Levy"}
print(type(dictionary1))
print(dictionary1)
print(dictionary1["name"])
print(dictionary1[1])
print(dictionary1[2])