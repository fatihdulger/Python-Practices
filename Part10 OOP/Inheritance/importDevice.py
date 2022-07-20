from devices2 import *
from devices2A import *


class MobileColour(MobilePhone):
    def __init__(self, phoneColor, phoneMake, phoneDesc, phoneModel, phonePrice):
        super().__init__(phoneMake, phoneDesc, phoneModel, phonePrice)
        self.color = phoneColor


mob1 = MobilePhone.MobileStorage("5PTB")
print(f"The storage is {mob1.memoryCard}")

phoneC = MobileColour("Blue", "Samsung", "Slim Phone", "Galaxy 10", 1500)
# MobileSize("6.7", "Samsung", "Slim Phone", "Galaxy 10", 1500)

print(
    f"My phone is {phoneC.make} and {phoneC.description}, model {phoneC.model} and cost £{phoneC.price} colour {phoneC.color} "
)