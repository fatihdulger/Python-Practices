# subroutine is a sequence of insructions/ code block to perform a specific
# task with an identifiable name
# A subroutine does not have a return statement
# def is a keyword used to define a subroutine, followed by the name of the subroutine
# It is not executed unless the subroutine is called.

"syntax    keyword   name "

def username():   # define is subroutine called username
    uName = input("Enter your username: ")
    print(f"Your username is {uName}") 

    ## we need to call this subroutine!!!!

username()  ## we called/invoked the subroutine -- this is now outside and it shoud work now. be careful with indentations.

# Task 1
# Exercise modify the code above to ask for user firstname, lastname, age and favourite movie
# Give the subroutine a suitable name like ...person, userDeatails...etc
# Call/invoke the subroutine

def userDetails():
    firstName = input("Enter your name: ").title()
    lastName = input("Enter your lastname: ")
    age = int(input("Enter your age: "))
    uMovie = input("Enter your fav movie: ")

    print(f"your personal details are {firstName, lastName, age} and favourite movie is {uMovie} ")

#userDetails()


