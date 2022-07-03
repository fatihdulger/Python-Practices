import math  # import the math library /class/module

radius = float(input("Enter radius: "))

area = math.pi * radius ** 2

print(f"the area is {area}")


# method 1
print(f"The area displayed is rounded to 2 decimal places {area:.2f}")
print(f"The area displayed is rounded to 3 decimal places {area:.3f}")

# Method 2

roundown = math.floor(area)
print(f"The area is rounded down to the nearest whole number {roundown}")

# Method 3

roundUp = math.ceil(area)
print(f"The area is rounded up to the nearest whole number {roundUp}")

# Method 4

print(f"The area is {area.__round__(2)}")