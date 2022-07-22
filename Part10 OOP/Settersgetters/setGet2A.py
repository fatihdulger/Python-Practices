class Developer():
 def __init__(self, devName, devSal):
  self.name = devName
  self.salary = devSal
  self.job = "None"

 # create getter and setter methods 
 def getName(self): # create getter method
  return self.name #returns the value passed from the parameter to the variable

 def getPay(self):
  return self.salary

 def getJob(self):
  return self.job


# create setter method
 def setJob(self, devJob): # declare devJob as a parameter
  self.job = devJob # devJob parammeter will set the value to the variable self.job(job)

dev1 = Developer("Jane Smith", 65000) #create an instance object from the Developer class

print(f"{dev1.name} is paid {dev1.salary} yearly")

# call/invoke the setJob method and pass in the argument

dev1.setJob("Python")

print(f"{dev1.name} is paid {dev1.salary} yearly, working as a {dev1.job} developer")