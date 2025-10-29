# Employee Class
# Properties: branch, salary, position, years_of_employment, bonus_eligible
# Methods: Yearly Salary Calculator based on bonus_eligible
# Methods: Tax Deduction Per Year (>50k, 5%, >100k, 10%, >200k, 15%)


class Employee:
    def __init__(self, name, branch, salary, position, years_of_emp, bonus_el, bonus_per):
        self.name = name
        self.branch = branch
        self.salary = salary
        self.position = position
        self.years_of_employment = years_of_emp
        self.bonus_eligible = bonus_el
        self.bonus_percentage = bonus_per

    def calculate_yearly_salary(self):
        if self.bonus_eligible == True:
            bonus = self.bonus_percentage * self.salary
            total_salary = (self.salary + bonus) * 12
        else:
            total_salary = self.salary * 12

        return total_salary

    def calculate_yearly_tax_deduction(self):
        if self.salary <= 50000:
            tax = 0.05
        elif self.salary <= 100000:
            tax = 0.1
        else:
            tax = 0.15

        yearly_salary = self.calculate_yearly_salary()
        total_tax = tax * yearly_salary
        print(f"{self.name} pays yearly tax of {total_tax}")


alex = Employee("Alex", 75000, "Department Head", "Kathmandu", True, 0.2)

total_salary = alex.calculate_yearly_salary()
print(f"The total yearly salary of {alex.name} is {total_salary}")
alex.calculate_yearly_tax_deduction()
