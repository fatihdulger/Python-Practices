try:
    num = 10
    num1 = 0
    answer = num/num1
    print(answer)

except ZeroDivisionError:
    print("Can't divide a number by zero")

finally:
    print("Closing")

