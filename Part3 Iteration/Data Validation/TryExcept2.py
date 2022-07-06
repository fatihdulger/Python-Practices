num = input("Enter a number: ")  # this is not an issue but if you put int around num and num1 see what happens;
num1 = input("Enter second number: ")
print(num + num1)
print(f"Your lucky number is {num}")

## will return error "ValueError"

""" num = int(input("Enter a number: "))  # this is not an issue but if you put int around num and num1 see what happens;
num1 = int(input("Enter second number: "))
print(num + num1)
print(f"Your lucky number is {num}")  """

## but try except will solve this issue;

try:
    num = int(input("Enter a number: "))  # this is not an issue but if you put int around num and num1 see what happens;
    num1 = int(input("Enter second number: "))
    print(num + num1)
    print(f"Your lucky number is {num}")

except ValueError:
    print("Please enter a number ")

print(f"Enjoy your day")   ## f is not necessary but it is good to have
    

