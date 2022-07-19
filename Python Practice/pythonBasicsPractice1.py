class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * self.length + 2 * self.width
    
class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length

square = Square(4)
square.area()
print(f"square area is {square.area()}")
rectangle = Rectangle(2,4)
rectangle.area()
print(f"rectangle area is {rectangle.area()}")

#### using super()

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * self.length + 2 * self.width

# Here we declare that the Square class inherits from the Rectangle class

class Square (Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

# here we ve used super() to call the __init__() of the Rectangle class, allowing you to use it in the Square class without repeating code.

square = Square(4)
square.area()

print(f"The area is {square.area()}")

