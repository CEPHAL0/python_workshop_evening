# Function 1 -> Deposit Amount
# Function 2 -> Withdraw Amount
# Function 3 -> Check Balance

balance = 10000

# Function Definition
def deposit_amount():
    amount = int(input("Enter the amount you want to deposit: "))
    balance += amount
    print(f"You have successfully deposited {amount}")

# Function Call
deposit_amount()

# Input Value
withdraw_amount_input = int(input("Enter the amount you want to withdraw: "))

# Function Definition 1
def check_withdraw_eligibility(amount):
    if amount > balance:
        print("Insufficient Balance")
    else:
        print("Sufficient Balance")

# Function Definition 2
def withdraw_amount(amt):
    # Function Call 1
    check_withdraw_eligibility(amt)
    balance -= amt
    print(f"You have successfully withdrawed {amt}")

withdraw_amount(amt=withdraw_amount_input)
