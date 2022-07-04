# selection is used to control the of the program 

score = 16 # int(input("enter a score:"))

if score > 25: # check the condition that score is greater than 25
    print(f"Good score {score}") # excuted if the condition is met.
print("closing") # executed regardless

# modify the code below using any three cmparison operator

if score != 25:  # check the condition that score is greater than 25
    print(f"Good score {score}")  # executed if the condition is met
print("closing not equal 25")
   
if score < 25:  # check the condition that score is greater than 25
    print(f"Good score {score}")  # executed if the condition is met
print("closing not equal 25")

if score == 25:  # check the condition that score is greater than 25
    print(f"Good score {score}")  # executed if the condition is met
print("closing not equal 25")

name = 'Bob'
age = 30
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
else:
    print('You are neither Alice nor a little kid.')