# Dictionary Way
marks = {}

subject_name_1 = input("Enter the subject 1 name: ")
marks[subject_name_1] = int(input(f"Enter the marks of {subject_name_1}: "))

subject_name_2 = input("Enter the subject 2 name: ")
marks[subject_name_2] = int(input(f"Enter the marks of {subject_name_2}: "))

subject_name_3 = input("Enter the subject 3 name: ")
marks[subject_name_3] = int(input(f"Enter the marks of {subject_name_3}: "))

full_marks = int(input("Enter the full marks of one subject: "))
number_of_subjects = len(marks)

total_obtained_marks = marks[subject_name_1] + marks[subject_name_2] + marks[subject_name_3]
total_full_marks = full_marks * number_of_subjects

percentage = (total_obtained_marks / total_full_marks) * 100

print(f"The obtained percentage is {percentage}%")
