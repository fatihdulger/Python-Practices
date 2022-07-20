class MobilePhone:  # class called MobilePhone
    def __init__(self, phoneMake, phoneDesc, phoneModel, phonePrice):   # constructor
        self.make = phoneMake
        self.description = phoneDesc
        self.model = phoneModel
        self.price = phonePrice


# create a class method
    def discount(self):  # jsut try delete self so it will not be called/invoked and below calcDisc will not be able to access above class !!!

        calcDisc = self.price * 0.8  ## since this is class method we can use  self.price without referencing and invoking 'self' in def discount() then this will be invoked and we can access above class
        "calcDisc = 1280 x 0.8 "
        print(f"the discounted price is {calcDisc}")

         # create an inner class

    class MobileStorage:
        def __init__(self, storageSize):
            self.memoryCard = storageSize

# now think how we can access to this above method??? 
"Method 0"

#create an instance object from the MobilePhone class/template
"Method 1"
myphone1 = MobilePhone("nokia", "Brick Phone", "3310", 1000).discount()

"Method 2"
myphone2 = MobilePhone("Samsung", "Slim Phone", "Galaxy 10", 1500).discount()
myphone2.discount()
print(f"The storage is {myphone2.make}")

#how do we access an inner class; line 18 it is class

myphone3 = MobilePhone("Iphone", "Fold Phone", "XR", 2000).MobileStorage("20GB")  # you can say 20 without quoatation marks.
print(f"The storage is {myphone3.memoryCard}")

myphone4 = MobilePhone.MobileStorage("1TB")
print(f"The storage is {myphone4.memoryCard}")