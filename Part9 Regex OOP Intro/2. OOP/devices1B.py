class MobilePhone:  # class called MobilePhone
    def __init__(self, phoneMake, phoneDesc, phoneModel, phonePrice):   # constructor
        self.make = phoneMake
        self.description = phoneDesc
        self.model = phoneModel
        self.price = phonePrice


# create an empty list
listOfPhones = []

while True:
    argmake = input("Enter phone make: ")
    argdesc = input("Enter phone description: ")
    argmodel = input("Enter phone model: ")
    argprice = float(input("Enter phone cost: "))
    # add phone and phone details to the list
    # Samsung Slim build Galaxy10 899.67
    listOfPhones.append(argmake + " " +argdesc + " "+argmodel +" "+ str(argprice) )
    # listOfPhones.append(f"{argmake} {argdesc} {argmodel} {str(argprice)}")
    anotherMobile = input("Enter another mobile phone? Y/N ").upper()

    if anotherMobile == "N": # if condition is met

        break # exits the loop so as not to add another mobile phone.
print(listOfPhones)

# create an object from the class mobile phone.
myPhone = MobilePhone(argmake, argdesc, argmodel, argprice)

for mobile in listOfPhones:
    print(mobile)

    with open(r"PYTHON\Part9 Regex OOP Intro\2. OOP\phonelist1.txt", "a") as file1: # this one uses FOR LOOP
        saveMobiles = file1.write(f"\n{mobile}")

with open("PYTHON\Part9 Regex OOP Intro/2. OOP/phonelist2.txt", "a") as file2: # this bit doesnt use for loop just writing in the list
    phones = str(listOfPhones)
    savePhones = file2.write(f"\n{phones}")


    