num = 2 # int(input("enter a number: "))
"num = 2 is the start value"

while num <= 20: # set the condition to check the numbr will increment until it gets to 20
    print(num)
    num += 1   # it will inrement starting from 2 until 20

    if num == 15: # set the condition that if true, will execute the break syntax below
        print("condition met")
        break # break out of the loop
    
    num += 1

    