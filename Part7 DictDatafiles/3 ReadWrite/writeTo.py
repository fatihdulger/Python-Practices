" WRITE to FILE"
# There are three modes for opening a file:
# r   for only reading files # only read files
# w   for only writing to files
# a   for adding to an existing file

with open(r"C:\Users\Ahmet Melih\fatihdulger1\PYTHON\Part7 DictDatafiles\3 ReadWrite\user1.txt", "w") as userFile1:

    writeContent = userFile1.write("I love python")  # use write method to write to file