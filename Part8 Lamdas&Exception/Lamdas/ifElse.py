compare = lambda num1: "Even number" if num1 % 2 == 0 else "odd number"
print(f"{compare(22)}")
print(f"{compare(21)}")

userCheck = lambda userName: print(f"Your user name is: {userName}") if len(userName) > 5 else print(f"Invalid: {userName}")  ## username is placeholder or argument userCheck is variable and this is lambda funciton.
name = input("Enter your user name: ")
userCheck(name)

substring = lambda subS: subS in "This is python"
print(f"Found {substring('this')}")
print(f"Found {substring('This')}")



