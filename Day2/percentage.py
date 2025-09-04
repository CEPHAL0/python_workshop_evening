marks = []

# user_enter_marks = float(input("Enter the marks of subject 1: "))
marks.append(float(input("Enter the marks of subject 1: ")))

message = "Enter the marks of subject 2: "
user_enter_marks = input(message)
user_enter_marks = float(user_enter_marks)
marks.append(user_enter_marks)

user_enter_marks = float(input("Enter the marks of subject 3: "))
marks.append(user_enter_marks)

user_enter_marks = float(input("Enter the marks of subject 4: "))
marks.append(user_enter_marks)

user_enter_marks = float(input("Enter the marks of subject 5: "))
marks.append(user_enter_marks)

total_obtained_marks = marks[0] + marks[1] + marks[2] + marks[3] + marks[4]
total_full_marks = 60 * 5

percentage = (total_obtained_marks / total_full_marks) * 100

print(f"The final percentage of student is {percentage}%")
