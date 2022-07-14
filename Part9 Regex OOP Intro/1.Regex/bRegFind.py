# Regular expressions are patterns that help a user match character combinations
# in text files and strings. You can use regular expressions to filter or find a
# specific pattern in the output of a  command or a document.

import re  # import the regex module

# #findALL = Return a list of all non-overlapping matches in the string.
# If one or more capturing groups are present in the pattern,
# return a list of groups; this will be a list of tuples if
# the pattern has more than one group.
# findall is the most appropriate one to use because search method finds only one matching findall scans thru the data and bring up.

sentence = "Take up one idea. One ideas at a time Off oof orE o2H"

# searchVariable = re.findall(r"o\w\w)




searchString = re.findall(r"o\w\w", sentence) # searches from start to the end of the string

# searchString = re.findall (r"o\w\w", sentence.lower())

print(f"SearCH result {searchString}")

# exercise  modify the findall method to use the following in the search

sentence1 = "Come up with ghee project. Ghert idea out of the blue the ghet is good ghost"

# \w+  
# #>>> is to return one or more character after the specified start character

searchString1 = re.findall(r"g\w+", sentence1)
print(f"SearCH result {searchString1}")

# \w*
# returns zero or more charachter after the specified start character. g\w* means i can return zero or word starting with g and anything then  others.

searchString2 = re.findall(r"g\w*", sentence1)
print(f"SearCH result {searchString2}")

# \w?
searchString3 = re.findall(r"g\w?", sentence1)
print(f"SearCH result {searchString3}")

# exercise  modify the findall method to use the following in the search

# \w+

# \w*

# \w?

# returns one or more character after the specified start character

searchString1 = re.findall(r"o\w+", sentence)

print(f"Search result {searchString1}")



# returns zero or more character after the specified start character

searchString2 = re.findall(r"o\w*", sentence)

print(f"Search result {searchString2}")



# returns zero or one character after the specified start character shaving the characters off

searchString2 = re.findall(r"o\w?", sentence)

print(f"Search result {searchString2}")