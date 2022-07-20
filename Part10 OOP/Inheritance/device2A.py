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

# create a child (inheritance) 
"Method 1"
class MobileCPU(MobilePhone): # passed in the name of the parent class (MobilePhone) as a parameter
    # passed in the MobilePhone parameters as child class parameters
    def __init__(self, phoneCPU, phoneMake, phoneDesc, phoneModel, phonePrice):
        #import the parent class constructor
        MobilePhone.__init__(self, phoneMake, phoneDesc,phoneModel,phonePrice)
        # local variable for the child class
        self.processor = phoneCPU

# how do we access an child class

"Create an instance object from the child class"
cpu1 = MobileCPU ("Snap Dragon", "Iphone", "Fold phone", "XR", 2000)

print(

    f"My phone is {cpu1.make} and {cpu1.description}, model {cpu1.model} and cost £{cpu1.price} has a {cpu1.processor} CPU"

)


# create a child (inherittance)
# "Method 2"
class MobileSize(MobilePhone):
     def __init__(self, phoneSize,phoneMake, phoneDesc, phoneModel, phonePrice):
         super().__init__(phoneMake, phoneDesc, phoneModel, phonePrice)
         self.screenSize = phoneSize

cpu2 = MobileSize("6.7", "Samsung", "Slim Phone", "Galaxy 10", 1500)

print(
 f"My phone is {cpu2.make} and {cpu2.description}, model {cpu2.model} and cost £{cpu2.price} screen {cpu2.screenSize} "
)

