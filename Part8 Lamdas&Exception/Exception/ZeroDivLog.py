import logging

#setlogging level

logging.basicConfig(
    filename= r"\C:\Users\Ahmet Melih\fatihdulger1\PYTHON\Part8 Lamdas&Exception\Exception\zDivLog.txt", level=logging.DEBUG
)



try:
    num = 10
    num1 = 0
    answer = num/num1
    print(f"The answer to {num} / {num1} : {answer}")
except ZeroDivisionError:
    print("Can't divide a number by zero")
    logging.error("User attempted to divide by Zero")
finally:
    print("Closing")