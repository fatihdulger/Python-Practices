
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
print(set1)

# add/update set items

set1.update(["Jane", "Em", "Jay", 345.6])
print(set1)

set1.remove(10)
print(set1)
set1.clear()
print(set1)

# use frozen to freeze set ( once set is frozen you cant do anything you cant add/remove/ you cant change)

fset = frozenset(set1)

print(set1)
#once it is set no changes can be made!!!

# declare  tuple and assigned different data type

tpl1 = ("a", "b", "c", "b", "c", "b", "c", "b", "c")  # 10, 12, -1, 23)
tpl2 = ("mytuple",)

print(type(tpl1))
print(type(tpl2))
# access the index value of a tuple
print(tpl1.index("b"))  # reaching index position is different
print(f"The index position of {tpl1[1]} is {tpl1.index("b")}")


# count items in a tuple
print(f"{tpl1.count('b'), 'b'} ")