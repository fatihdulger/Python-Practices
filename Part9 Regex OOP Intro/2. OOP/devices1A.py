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

class MobilePhone:  # class called MobilePhone

    def __init__(self, phoneMake, phoneDesc, phoneModel, phonePrice):  # constructor
        # all variables are local only to the class constructor
        # variables: make, description, model and price
        self.make = phoneMake
        self.description = phoneDesc
        self.model = phoneModel
        self.price = phonePrice


# how do we access properties/variables and values inside the MobilePhone class ?

# myPhone1 = MobilePhone()  # create an object from the MobilePhone class \\ we should move the function call down after variable declarations

# myPhone1.make = input("Enter phone make: ")
# myPhone1.desc = input("Enter phone description: ")
# myPhone1.model = input("Enter phone model: ")
# myPhone1.price = float(input("Enter phone cost: "))

argmake = input("Enter phone make: ")
argdesc = input("Enter phone description: ")
argmodel = input("Enter phone model: ")
argprice = float(input("Enter phone cost: "))

myPhone1 = MobilePhone(argmake, argdesc, argmodel, argprice) # create an object from the MobilePhone class

print(f" Make: {argmake} Desc: {argdesc} Model: {argmodel} Price: {argprice}")

myPhone2 = MobilePhone(
    input("Enter phone make: "),
    input("Enter phone description: "),
    input("Enter phone model: "),
    float(input("Enter phone cost: ")),

)
#print(f" Make: {myPhone2.make} Desc: {argdesc} Model: {argmodel} Price: {argprice}")

print(
    f"My phone is {myPhone2.make} and {myPhone2.description}, model {myPhone2.model} and cost £{myPhone2.price}"
)

myPhone3 = MobilePhone("TestPhone", "TestDesc", "TestModel", 1234) # argument passed in as hardcoded values 
print(
    f"My phone is {myPhone3.make} and {myPhone3.description}, model {myPhone3.model} and cost £{myPhone3.price}"
)

myPhone4 = MobilePhone("nokia", "Brick Phone", "3310", 15) # argument passed in as hardcoded values 
print(
    f"My phone is {myPhone4.make} and {myPhone4.description}, model {myPhone4.model} and cost £{myPhone4.price}"
)
