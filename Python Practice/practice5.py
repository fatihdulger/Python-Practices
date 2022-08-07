# Task1:  Create two lists
# •	Subtract items in one list by items in another list
# •	Divide items in one list by items in another list
# •	Multiply items in one list by items in another list

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

list1_2 = [
    list2[i] - list1[i]
    for i in range(len(list1)) # task1_1
    
]
print(list1_2)

for i in range(len(list2)):
    list3 = list2[i] / list1[i]
    print(list3)  # task 1_2


myList = [*range(1,21, 1)]
print(myList)

# task 2 modify the program below

varNum = int(input("Enter a number: "))
varConvert = chr(varNum) # invoke/call the chr function to convert number to an ascii
varMsg = varMsg + varConvert

print(varMsg)
#•	Use the order ASCII method to return the decimal equivalent of a character

# Task3: Write a program that will:
# •	Create a 2D list with 4 rows 
# •	Each row must hold 6 items each
# •	Print the 2nd, 4th and last item in from row 0
# •	Print the 2nd, 5th and last item from row 1
# •	 Print the 1nd, 3rd and 5th from row 3
# •	Print out all items in row 0 with using their index position
# •	Amend/update 2 items in each list using their rows and indexes
# •	Add two more items to each list using append function

list5 = [[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[3,5,6,7,8,9]]

print(list5[0][1], list5[0][3], list5[0][-1])

print(list5[1][1], list5[1][4], list5[1][-1])





