# There are three modes for opening a file:
# r   for only reading files # only read files
# w   for only writing to files
# a   for adding to an existing file

"open method opens the file"

# Part 7 DictDatafiles\3 ReadWrite\names.txt
#C:\Users\Ahmet Melih\fatihdulger1\PYTHON\Part7 DictDatafiles\3 ReadWrite\names.txt

# Method 1
"variableName = open(folderPath/...../filename.........., mode)"

"variableName = open(folderPath/......../filename..........., mode)"

userFile = open(r"C:\Users\Ahmet Melih\fatihdulger1\PYTHON\Part7 DictDatafiles\3 ReadWrite\names.txt", "r")  ### if you use backslash  you need to put r before quotation mark userFile = open(r"Part 7 .....)

fileContent = userFile.read() # read method read the content of a file

print(fileContent)

# Method 2: Using context manager

with open(r"C:\Users\Ahmet Melih\fatihdulger1\PYTHON\Part7 DictDatafiles\3 ReadWrite\names.txt", "r") as userFile1:
    fileContent = userFile1.read()
    print(fileContent)