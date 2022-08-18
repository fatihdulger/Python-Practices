from guizero import *


# from guizero import App, Text, TextBox, PushButton (main steps to go thru and build)



# create an instance object called app from the App class/template

app = App(title="Add Numbers", bg="cadetblue", layout="auto")

# create an instance object called lblTxt from the Text class/template

lblTxt = Text(app, text="Enter First Number", color="red")

# create an instance object called txtBox1 from the TextBox class/template

txtBox1 = TextBox(app )

# create an instance object called txtBox2 from the TextBox class/template

txtBox2 = TextBox(app,  text="Enter Second Number")


displayAns = Text(app, text="Answer will be displayed here", width=50)

def addition():
  num1 = txtBox1.value
  num2 = txtBox2.value

  answer = int(num1) + int(num2)
  displayAns.value = answer

btnAdd = PushButton(app, command=addition, text="Add") # command=addition this doesnt take any braces
app.display()
