class Developer:
    def __init__(self):
        self.name = ""
        self.salary = ""

        #create getter methods
    def getName(self): # create getter method!!! whenever we say self >>> we refer to constructor
        return self.name # return the value passed to the variable
    
    def getPay(self): # create getter method
        return self.salary # return the value passed to the variable

# how do we access the class
"Create an instance object"

dev1 = Developer()
dev1.name = "Anna"
dev1.salary = 12345

print(f"{dev1.name} is paid {dev1.salary} as a developer")

dev2 = Developer()
dev2.name = "Jane"
dev2.salary = 456789

print(f"{dev2.getName()} is paid {dev2.getPay()} as a developer")


class Developer:
    def __init__(self):
        self.name = ""
        self.salary = ""

        #create getter methods
    def getName(self): # create getter method!!! whenever we say self >>> we refer to constructor
        return self.name # return the value passed to the variable
    
    def getPay(self): # create getter method
        return self.salary # return the value passed to the variable
    
    
    def setJob(self, myJob):
        self.job = myJob

    # create a setter method
    def getJob(self):
        return self.job



dev3 = Developer()
dev3.name = "Paul"
dev3.salary = 10335
dev3.setJob("Python")

print(f"{dev3.name} is paid {dev3.salary} as a {dev3.job} developer")



