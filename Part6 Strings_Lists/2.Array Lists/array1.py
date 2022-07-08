# An array holds multiple items under one name.
# An array is a static data structure.
# An array is fixed in size and can only contain data of the same type.
# The contents can be changed, but items cannot be added or deleted.
# The structure must remain fixed

# Python does not have any native way of storing arrays. it has workarounds

array1 = ["Amy", 1,2,3,12.6, "jane"] # this is list of different items.

arrayDigits = [1,2,3,4,5,6,61] # an array based on implementation

print(type(array1))
print(type(arrayDigits))
for arrayItems in array1:
    print(arrayItems)
