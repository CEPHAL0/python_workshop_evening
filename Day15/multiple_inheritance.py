# Base Entities:
# Person → shared parent
# Properties: name, age, email

# Student(Person)
# Unique: student_id, major, gpa

# Teacher(Person)
# Unique: employee_id, subject, salary

# Administrator(Person)
# Unique: role, office_number

# Example multiple inheritance:
# TeachingAssistant(Student, Teacher) → shares properties and behavior of both.

# Hierarchical Multiple Inheritance
# Base Class
class Person:
    name = ''
    age = 0
    email = ''

# Single Inheritance
class Student(Person):
    student_id = ''
    major = ''
    gpa = ''

# Single Inheritance
class Teacher(Person):
    employee_id = ''
    subject = ''
    salary = 0.0

# Single Inheritance
class Administrator(Person):
    role = ''
    room_number = 0

# Hierarchical Multiple Inheritance
class TeachingAssistant(Student, Teacher):
    def __repr__(self):
        information = f"""
        Name: {self.name}
        Age: {self.age}
        Email: {self.email}
        Major: {self.major}
        GPA: {self.gpa}
        Employee ID: {self.employee_id}
        Subject: {self.subject}
        Salary: {self.salary}
        """
        return information

asst1 = TeachingAssistant()
asst1.name = 'Alice'
asst1.age = 26
asst1.email = 'alice@ny.com'
asst1.major = 'CS'
asst1.gpa = '3.6'
asst1.employee_id = '451231'
asst1.salary = 45000
asst1.subject = 'Discrete Structures'

print(asst1)