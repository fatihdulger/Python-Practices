""" To understand the meaning of classes we
have to understand the built-in __init__() function.
All classes have a function called __init__(), which is
 always executed when the class is being initiated.
 Use the __init__() function to assign values to object
 properties, or other operations that are necessary to do
 when the object is being created:  """

# what is a constructor in python?
# it is a method that is called when an object is created
# This method is defined inside the class and can be used to initilise variables

# class is a blueprint/template
# create a class called MobilePhone

class MobilePhone:   ## create a class called MobilePhone
    def __init__(self):   #constructor
        #all variables are local only to the class constructor
        # variables: make, description, model and price
        self.make = "Samsung"
        self.description = "Slim build"
        self.model = "Galaxy s10+"
        self.price = 896.12

#how do we access properties/variables and values inside the MobilePhone class ?

myPhone1 = MobilePhone() #create an object from the MobilePhone class

"use the object(myPhone1) to access properties/variables and values inside the MobilePhone class "

print(myPhone1.make)
print(myPhone1.description)
print(myPhone1.model)
print(myPhone1.price)

myPhone2 = MobilePhone()
myPhone2.make = "Apple"
myPhone2.description = "IPS Display"
myPhone2.model = "12 Pro Max"
myPhone2.price = 1199.99

print(myPhone2.make)
print(myPhone2.description)
print(myPhone2.model)
print(myPhone2.price)

myPhone3 = MobilePhone()
myPhone3.make = input("Enter phone make: ")
myPhone3.description = input("Enter phone description: ")
myPhone3.model = input("Enter phone model: ")
myPhone3.price = float(input("Enter phone cost: "))

print(myPhone2.make)
print(myPhone2.description)
print(myPhone2.model)
print(myPhone2.price)

print(f"My phone is {myPhone3.make} and {myPhone3.description}, model {myPhone3.model} and cost £{myPhone3.price}")

