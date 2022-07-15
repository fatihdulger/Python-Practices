# file1 = open("Part9 Regex & OOP Intro/2. OOP/Code Review/data.txt", "r")
# create variable file1 to pass the file path with read option
# readfile = file1.read()                      # read method display read the file
# print(readfile)
# file1.close
data = []  # create an empty list
print("This is a list before adding data ", data)
with open("Part9 Regex _OOP Intro/Code Review/data.txt", "r") as file1:
    # readFile1 = file1.read()

    for findUser in file1:
        findUser = findUser.strip()  # r.strp()
        findUser = findUser.split(" ")
        data.append(findUser)
print("THis is a list after adding data ", data)
# file1.close()

# print()
print("From memory ", data)
user = input("Enter a player name:")

playerlocation = ""

for item in data:

    if user in item:
        location = data.index(item)
lName = data[location][1]
age = data[location][2]

print(f"{user}, your lastname is {lName} and you are {age} years old")


# list = ["ANNA", "Lucy", "joe"]
# print(list.index("ANNA"))
# print(list.index("Lucy"))
# print(list.index("joe"))
