# Take the input marks of 3 subject
subject_1 = int(input("Enter the subject 1 marks: "))
subject_2 = int(input("Enter the subject 2 marks: "))
subject_3 = int(input("Enter the subject 3 marks: "))

full_marks = int(input("Enter the full marks of 1 subject: "))

# Calculate the total obtained marks
total_obtained_marks = subject_1 + subject_2 + subject_3

# Calculate the total full marks
total_full_marks = full_marks * 3

# Calculate the percentage
percentage = (total_obtained_marks/total_full_marks) * 100

# Print the output in proper format
print(f"The obtained percentage is {percentage}%")


# List Way
subjects = []

input_marks = int(input("Enter the marks 1: "))
subjects.append(input_marks)

input_marks = int(input("Enter the marks 2: "))
subjects.append(input_marks)

input_marks = int(input("Enter the marks 3: "))
subjects.append(input_marks)

full_marks = int(input("Enter the full marks of one subject: "))
number_of_subjects = len(subjects)

total_full_marks = full_marks * number_of_subjects
total_obtained_marks = subjects[0] + subjects[1] + subjects[2]

percentage = (total_obtained_marks / total_full_marks) * 100

print(f"The obtained percentage is {percentage}%")


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
