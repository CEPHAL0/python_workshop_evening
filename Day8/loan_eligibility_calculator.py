# Loan Eligibility Calculate
# Age > 25
# Monthly salary should be at least 10% of loan
# Chosen interest rate should not be less than 13%

# or

# Age > 40 and Monthly salary more than 50% of loan

# Input -> Date of Birth (Year), Monthly salary, Chosen Interest Rate, Loan Amount
# Output -> Eligible / Not Eligible


date_of_birth = int(input("Enter the date of birth: "))
monthly_salary = float(input("Enter the monthly salary: "))
loan_amount = float(input("Enter the loan amount: "))
chosen_interest = float(input("Enter the chosen interest rate: "))

# Calculate the age
age = 2025 - date_of_birth

age_greater_than_25 = age > 25
age_greater_than_40 = age > 40
monthly_salary_greater_than_10 = monthly_salary >= (0.1 * loan_amount)
monthly_salary_greater_than_50 = monthly_salary >= (0.5 * loan_amount)
chosen_interest_not_less_than_13 = chosen_interest < 13

first_eligibility_condition = age_greater_than_25 and monthly_salary_greater_than_10 and chosen_interest_not_less_than_13

second_eligibility_condition = age_greater_than_40 and monthly_salary_greater_than_50

eligibility = first_eligibility_condition or second_eligibility_condition

if eligibility:
    print("Eligible")
else:
    print("Not eligible")

if (
    (age > 25) and (monthly_salary >= (0.1 * loan_amount)) and (chosen_interest < 13)
    ) or (
        (age > 40) and (monthly_salary >= (0.5 * loan_amount))
    ):
    print("Eligible")
else:
    print("Not eligible")
