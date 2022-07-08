from array import *

# An array holds multiple items under one name.
# An array is a static data structure.
# An array is fixed in size and can only contain data of the same type.
# The contents can be changed, but items cannot be added or deleted.
# The structure must remain fixed

# Python does not have any native way of storing arrays. it has workarounds

arrayDigits = array('i', [1,2,3,4,5,6,61])  ## i  is array code

print(type(arrayDigits)) # class 'array.array'

for arrayItems in arrayDigits:

    print(arrayItems)

    ## by the way Abdul never used this array  he used list