import time
userName = input("Enter Username")
fName = input("Enter Full name")
userAge = int(input("Enter User age"))

with open(r"C:\Users\Ahmet Melih\fatihdulger1\PYTHON\Part7 DictDatafiles\3 ReadWrite\userDetails.txt", "a") as userFile1:
    # method 1
    writeContent = userFile1.write(
        f"\n{userName}\n{fName}\n{userAge}"
    )  # use write method to write to file

# Method 2

userFile1.write("\n" + userName + " " + fName + " " + str(userAge)  )

# Method 3

userData = []
userData.append(userAge)
userData.append(fName)
userData.append(userAge)
strData = str(userData) # converts list to string

time.sleep(3)
userFile1.write(f"\n {strData}")

""" name = "Jane"
    print(list(name))"""

time.sleep(3)

searchFile = input("Enter Username ")
with open(r"C:\Users\Ahmet Melih\fatihdulger1\PYTHON\Part7 DictDatafiles\3 ReadWrite\userDetails.txt", "r") as userSearch:
    readfile = userSearch.read()

if searchFile in readfile:
    print(f"Found{searchFile}")
else:
    print("Text not Found")


