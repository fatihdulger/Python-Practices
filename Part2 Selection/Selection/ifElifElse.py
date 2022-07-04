score = int(input("Enter your score: "))

if score >= 75: # check if score is greater than equal to
    grade = "A" # create a variable an assign it the value A

elif score >= 60:
    grade = "B"

elif score >= 50:
    grade = "C"
else:
    grade = "F"

print(f"You scored {score} and your grade is {grade}")