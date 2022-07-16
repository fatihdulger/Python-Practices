
# Task1: 
# Write a new program which will create a list with 10 city names. >>> lstCity10 = ["London", "Cambridge", "Oxford", "Bristol", "Liverpool", "Manchester", "Reading", "Brighton", "Edinburgh", "Cardiff"]
# •	Print the list with all the items showing on one line. >>> print(lstCity10)
# •	Insert a new city in index position 4 >>>lstCity10.insert(3,"York")
# •	Print out the fourth item in the list by it index position. >> print(lstCity10[3])
# •	Print out the sixth item in the list by its value. >>print("Liverpool")
# •	Remove any  two cities from the list >>>del lstCity10[5:7]
# •	How can you print the 4th,5th,6th and 7th cities in the list >>print(lstCity10[3:7])
# •	Return the length of the list >>> print(len(lstCity10))
# •	Sort the list in ascending order lstCity10.sort() print(f"Sorting cities in ascending order {lstCity10}")
# •	Sort the list in descending order >>> lstCity10.sort(reverse=True)
# Note: for every list manipulation print the list


lstCity10 = ["London", "Cambridge", "Oxford", "Bristol", "Liverpool", "Manchester", "Reading", "Brighton", "Edinburgh", "Cardiff"]
print(lstCity10)
lstCity10.insert(3,"York")
print(lstCity10)
print(lstCity10[3])
print(lstCity10[5])
print("Liverpool")
lstCity10.append('Istanbul')
print(lstCity10)
del lstCity10[5:7]
print(lstCity10)
print(lstCity10[3:])
print(f"The length of the list is: {len(lstCity10)}")
print(len(lstCity10))
print(lstCity10)

lstCity10.sort()
print(f"Sorting cities in ascending order {lstCity10}")

lstCity10.sort(reverse=True)
#print(f"Sorting cities in descending order {lstCity10}")


#Task2
#  You have been provided with the following string of characters stored in the variable as shown below 
# userString = " Python is my third programming language"
# •	Print the 1st, 3rd, 6th, 9th and 11th characters from the string (userString) provided above. >>>print(userString[1], userString[3], userString[6], userString[9], userString[11])
# •	Return the length of the string >>> print({len(userString)})
# •	Slice the string to print between the 3rd and 11 characters >>> print(userString[2:10])
# •	Omit the last  and  then second to last characters from your string in your print out  >>> print(userString[-2:])
# •	Print up to the 15 character from your string. >>> print(userString[:15])
# •	Find the start index position of the substring “third”  >>> print(userString[2:10])
# •	Print out the string in all capital letters.  >>> print(f"{userString.upper()}")
# •	Print out the string in all non lower case letters. 
# •	Print out the first letter of all the sub strings in capital letters. 
# •	Replace the substring “third” to so that the string will reflect if it is your first or second…etc """

userString = " Python is my third programming language"
print(userString)

print(userString[1])
print(userString[1], userString[3], userString[6], userString[9], userString[11]) # task 2-1
print(userString[3::3])
print({len(userString)}) # task 2-2

print(userString[2:10]) # task 2-3
print(userString[-2:]) #task 2-4
print(userString[:15]) #task 2-5

index = userString.index('third')
print(index)
print(f"{userString.index('third')}") #task 2-6
print(f"{userString.upper()}") # task 2-7
print(f"lower {userString.lower()}") #task 2-8
print(f"firstUpper {userString.title()}") # task 2-9
print(f"Replace {userString.replace('third', 'second')}") #task 2-10










