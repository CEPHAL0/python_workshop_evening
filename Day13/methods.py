# Procedural Way (Function Based Approach)
def percentage_calculator(name, marks1, marks2, marks3, total_marks):
    sum_marks = marks1 + marks2 + marks3
    total_marks = total_marks * 3
    percentage = (sum_marks/total_marks) * 100

    print(f"{name} scored {percentage}%")

# OOP Way
class Student:
    name = ''
    marks1 = 0
    marks2 = 0
    marks3 = 0
    total_marks = 0
    percentage = 0

    # Method
    def percentage_calculator(self):
        sum_marks = self.marks1 + self.marks2 + self.marks3
        total_marks = self.total_marks * 3
        percentage = (sum_marks / total_marks) * 100

        print(f"{self.name} scored {percentage}%")
        self.percentage = percentage
    
    # Method 2
    def pass_fail(self):
        if self.percentage < 45:
            print("Fail")
        else:
            print("Pass")

student1 = Student()
student1.name = 'Sharad'
student1.marks1 = 50
student1.marks2 = 60
student1.marks3 = 65
student1.total_marks = 75

print(student1.percentage)
student1.percentage_calculator()
print(student1.percentage)

student1.pass_fail()