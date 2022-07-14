import re  # import the regex module

sentence = "Take two up one idea. One idea at a time"

"""match Try to apply the pattern at the start of the string,
returning a Match object, or None if no match was found.
"""
# searchString = re.search(r"o\w\w", sentence.upper())

searchString = re.match(r"T\w\w", sentence)

# The group method is a method on the result that comes back which gives the exact

# substring that matches the pattern specified in the search

print(f"Seard result {searchString.group()}")