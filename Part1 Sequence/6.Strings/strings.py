from asyncio.proactor_events import _ProactorBaseWritePipeTransport


s1 = "I am a python programmer"
s2 = 'I am a python programmer with single quote'
s3 = """I am a python programmer, python is great, widely use for all things software related. 
Data science, full stack and front end"""
s4 = " How are you "

print(s1[10], s2[16], s3[20]) # print characters by index position


# exercise: print two characters from each string by index

print(s1[1], s2[5])

print(s1[5:8], s2[1:3])
print({len(s2)})

print(s2[1:3])  # start index and end index

print(s2[1:])  # start index and no end index

print(s2[:])  # no start index and no end index

print(s2)  # this is same as one above

print(s1[5:-1])
print(s1[-2:-1])

print(s1[5:-2])

# slicing string using start and end index and specify the steps

print(s2[1:15:3]) #start and end index, then step (every third character)
print(s2[1:20:2])

s5 = "Dangerous"
print(s5[1:10:2]) # start and end index, then step evry 2nd characters
print(s5[1::2]) # start index and step value
print(s5[::2]) # jsut the step


" How are you "

# stripping white spaces
print(s4)

print(s4.lstrip()) # strip white spaces on left side

print(s4.rstrip()) # strip white space on the right side

print(s4.strip()) # strip white space on both sides

# count a specific character

print(s3.count("a")) # returns the number of from the string

# Use upper , lower, and title methods

print(f"Upper Case{s4.upper()}")

print(f"Lower Case{s4.lower()}")

print(f"Title Case{s4.title()}")

# replace a substring 
print(s4.replace("How", "Where"))


txt = "I am jumping"

print(txt.lstrip) # this is not applicable it would be if there was space on the left
txt1 = "".join(txt.split())  # print(txt.replace(" ", "")) this can also work instead
print(txt1)


# index finding: finding out first index of any substring

index = userString.index('third')
print(index)