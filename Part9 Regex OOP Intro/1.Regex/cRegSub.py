import re  # import the regex module

sentence = "Take up one ideally on. One idea at o a time Off oOf overturn overt oranges orE o2H Ones ideas oo"

# sub = Return the string obtained by replacing the leftmost
# non-overlapping occurrences of the pattern in string by the replacement repl

print(f"Original string {sentence}")
searchString = re.sub(r"one", "two", sentence.lower())
print(f"Search result {searchString}")