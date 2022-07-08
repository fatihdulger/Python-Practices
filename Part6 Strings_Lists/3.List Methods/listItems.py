"i   =   0,1,2,3,4...." ## indext position

aList = [1,2,3,4,5,6] 

bList = [7,8,9,10,11,12]

print(aList) # [1, 2, 3, 4, 5, 6]

print(bList) # [7, 8, 9, 10, 11, 12]
" Add value of items in aList and bList"

listAB = [
    # alist[0][1][2]
    # bList
    aList[i] + bList[i]
    for i in range(len(aList)) # be careful you are referencing to aList if it has less items it would be problem!!! it hasto be more items.
]

print(listAB) # will return 1 +7 = 8 so on and so forth [8, 10, 12, 14, 16, 18]

# combine/join two list

joinList = aList + bList  # plus operation 

print(f"Joined/Combined List\n{joinList}")

sliceJoinItems = aList[0:2] + bList[0:3]
print(f"Joined Combined List\n{sliceJoinItems}")


cList = [1,2,3,10,11,4,5,6]
dList = [7,8,9,10,11,12,3,4,5]

commonItems = [nums for nums in cList if nums in dList]
commonItems.sort()
commonItems.sort(reverse=True)
print(f"The common list items are shown below\n{commonItems}")


namesA = ["Anna", "Lucy", "Jane"]
namesB = ["Anna", "Lucy", "Amy"]
#names = input("Enter name to search for: ")
commonNames = [names for names in namesA if names in namesB]   # names is variable you can use test or numbr or whatever

print(f"The common list items are shown below\n{commonNames}")
commonNames = [  for  in namesA if names in namesB]   # names is variable you can use test or numbr or whatever

print(f"The common list items are shown below\n{commonNames}")

namesA = ["Annan", "Lucy", "Jane"]

namesB = ["Anna", "Lucian", "Em", "Jane"]

names = input("Enter name to search for: ")

commonNames = [names for names in namesA if names in namesB]

# commonItems.sort(reverse=True)

print(f"The common list items are shown below\n{commonNames}")