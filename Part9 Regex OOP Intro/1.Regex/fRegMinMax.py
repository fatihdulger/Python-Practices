import re

# The curly braces "{}" RegEx use to specify a minimum and maximum  --- this is important 
# number of occurrences of the preceding RegEX  {min, max}, {max}

# you can use this with split combinator \d ****

sentence = "Take up 02-12-2022 one idea. One idea 2-06-20 at a time 8-06-2021"
# 0-00-00 , 00-00-0000
# 0-00-0000, 00-00-0000

searchString = re.findall("\d{1,2}-\d{1,2}-\d{2,4}", sentence) # seraches from start to the end of the string
print(f"Search result {searchString}")
### we used findall because because we wanted to make it 

searchString = re.findall("\d{1,2}-\d{1,2}-\d{4}", sentence) # seraches from start to the end of the string
print(f"Search result {searchString}")

