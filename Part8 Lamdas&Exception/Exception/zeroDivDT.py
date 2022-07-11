import logging
import time
#setlogging level

logging.basicConfig(
    filename=r"PYTHON\Part8 Lamdas&Exception\Exception\fatih.log", level=logging.DEBUG
)
#PYTHON\Part8 Lamdas&Exception\Exception\zeroDivDT.py


try:
    num = 10
    num1 = 0
    answer = num/num1
    print(f"The answer to {num} / {num1} : {answer}")
    logging.info(

        f"on {time.asctime()}\nDivision in progress {num} / {num1} : {answer}"

    )
except ZeroDivisionError:
    print("Can't divide a number by zero")
    logging.error(
        
        f"On{time.asctime()} : Error\nUser attempt to divide by Zero"
        "User attempted to divide by Zero")
finally:
    print("Closing")

# Abdul's working paths and program
    """import logging

import time



# set logging level

logging.basicConfig(

    filename="Part8 Lambdas&Exception/Exception/divdt.log", level=logging.DEBUG

)



try:

    num = 10

    num1 = 0

    answer = num / num1

    print(f"The answer to {num} / {num1} : {answer}")

    logging.info(f"On {time.asctime()}\nDivision in progress {num} / {num1} : {answer}")

except ZeroDivisionError:

    print("Can't divide a number by zero")

    logging.error(f"On{time.asctime()} : Error\nUser attempt to divide by Zero")

finally:

    print("Closing")"""