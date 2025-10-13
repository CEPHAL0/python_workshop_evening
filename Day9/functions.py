# Functions - Reusable Blocks of Code with dynamic input and output
# Mostly used to avoid repeating code for doing the same task
# Good Practice of function - KISS (Keep It Simple Stupid)

marks_1 = int(input("Enter the marks of subject 1: "))
marks_2 = int(input("Enter the marks of subject 2: "))
marks_3 = int(input("Enter the marks of subject 3: "))
marks_4 = int(input("Enter the marks of subject 4: "))
marks_5 = int(input("Enter the marks of subject 5: "))
marks_6 = int(input("Enter the marks of subject 6: "))


# Function Definition
def pass_fail_check(marks):
    if marks < 40:
        print("Fail")
    else:
        print("Pass")

# Function Call
pass_fail_check(marks=marks_1)
pass_fail_check(marks=marks_2)
pass_fail_check(marks=marks_3)
pass_fail_check(marks=marks_4)
pass_fail_check(marks=marks_5)
pass_fail_check(marks=marks_6)

# Function Definition
def percentage_calculator(m1, m2, m3, m4, m5, m6):
    sum_marks = m1 + m2 + m3 + m4 + m5 + m6
    total_full_marks = int(input("Enter the full marks of one subject: "))
    total_full_marks =  total_full_marks * 6

    percentage = (sum_marks/total_full_marks) * 100
    print(f"The percentage is {percentage}%")

# Function Call
percentage_calculator(m1=marks_1, m2=marks_2, m3=marks_3, m4=marks_4, m5=marks_5, m6=marks_6)