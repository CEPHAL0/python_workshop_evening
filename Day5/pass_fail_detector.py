# Input the marks of multiple subjects
subject1 = int(input("Enter the marks of subject 1: "))
subject2 = int(input("Enter the marks of subject 2: "))
subject3 = int(input("Enter the marks of subject 3: "))

# Input the total marks of one or all subjects
total_marks = int(input("Enter the full marks of one subject: "))

# Calculate the percentage
percentage = ((subject1 + subject2 + subject3) / (total_marks * 3)) * 100

# Determine pass or fail, Pass if percentage > 40 otherwise Fail
if percentage >= 40:
    print("Fail")
else:
    print("Pass")


# Division Determine based on the marks (multiple if else)
if percentage > 90:
    print("Distinction")
elif percentage > 80:
    print("First Division")
elif percentage > 70:
    print("Second Division")
elif percentage > 60:
    print("Third Division")
else:
    print("Fail")