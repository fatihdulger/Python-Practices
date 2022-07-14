# Regular expressions are patterns that help a user match character combinations
# in text files and strings. You can use regular expressions to filter or find a
# specific pattern in the output of a  command or a document.

import re  # import the regex module

"""\w = any alpha numeric char(any digits/character) = A-Z. Returns a match if the string 
contains alphanumeric characters including underscores. 
For example,\w will match a, b, c, d, 1, 2, 3, etc"""

sentence = "Take up one idea. One idea at a time"
# searchVariable = re.search(r"o\w\w)
# searchVariable = re.search(r"w\w\w)

"""search() = Scan through string looking for a match to the pattern, returning a Match object,
or None if no match was found."""

searchString = re.search(r"o\w\w", sentence.upper())  # re.search is the method for searching if string is compatible with our regex rule. finding 1st match
searchString = re.search(r"o\w\w", sentence) 

# The group method is a method on the result that comes back which gives the exact
# substring that matches the pattern specified in the search

print(f"Search result {searchString.group()}")