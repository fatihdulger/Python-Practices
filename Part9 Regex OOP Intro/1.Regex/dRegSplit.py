import re

sentence = "Take up one idea2lly on. One ide0a at o a time Off oOf over4turn overt or8anges orE o2H Ones ideas oo"

#split
"""

\d  = 0-9 , \D = non digit characters, \s = white space , \S = non white space,
Matches the preceding character one or more times.
The working of the + character is similar to *, but the +
character omits the pattern if the character doesn't occur.
For example, abc+ will match abc, abcc, abccc, etc.  """

print(f"Original string {sentence}")

searchString = re.split(r"\d",sentence)

print(f"Search result {searchString}")

# exercise modify the split method to pass in any of the three characters to perform a split

#  \D = non digit characters, \s = white space , \S = non white space

sentenceA = "In reg4rds to cl!mate ch4nge, we need r0bu5t acti0n"


print(f"Original string {sentenceA}")

searchString1 = re.split(r"\d",sentenceA)

print(f"Search result {searchString1}")



searchString2 = re.split(r"\s",sentenceA)

print(f"Search result {searchString2}")



searchString3 = re.split(r"\D",sentenceA)

print(f"Search result {searchString3}")

searchString4 = re.split(r"\S",sentenceA)

print(f"Search result {searchString4}")