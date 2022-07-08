# chr(): takes a decimal and returns the ascii equivalent
# ord(): takes a character and returns the decimal equivalent

aChar = input("Enter a character: ")
converAchar = ord(aChar)
print(converAchar)

alphabetList = []  # create an empty list

for letters in range(48, 123):
    alphabetList.append(chr(letters))

print(alphabetList)

def alphabets():   # writing function  - study this.
    for letters in range(48, 123):
        alphabetList.append(chr(letters))
    return alphabetList

print(alphabets())

