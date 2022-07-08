courseName = "Python" # input ("enter course name: ").title()
userSearch = "Pyt" # input("enter course to search for: ").title()

if userSearch in courseName:
    print(f"Found {userSearch}")
else:
    print(f"Not Found {userSearch}")   ## this will return pyt found if youput 

# Exercise find a vowel (a,e,i,o,u) in your full name

fullName = "Fatih Dulger"
vowels = ['a','e','i','o','u']

for x in vowels:
    if x in fullName:
        print(x)
    else:
        print(f"not found (x)")





fullName = "Fatih Dulger"
vowels = ['a','e','i','o','u']

if vowels in fullName:
    print(f"Found {vowels}")
else:
    print(f"Not Found {vowInName}")
