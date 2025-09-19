# ATM Machine
menu = """
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
"""

# Initialize the variable for first time
option = ""
balance = 1000


while option != "4":
    # Print Menu
    print(menu)

    # Ask for option
    option = input("Enter the option: ")

    if option == "1":
        print(f"Your balance is Rs. {balance}")

    elif option == "2":
        deposit_amount = int(input("Enter the amount you want to deposit: "))
        balance += deposit_amount
        print(f"You have deposited Rs.{deposit_amount} successfully")

    elif option == "3":
        withdraw_amount = int(input("Enter the amount you want to withdraw: "))

        if balance < withdraw_amount:
            print("Cannot withdraw amount greater than balance")
        else:
            balance -= withdraw_amount
            print(f"You have withdrawed Rs.{withdraw_amount} successfully")
            
    elif option == "4":
        print("Thank you for visiting us!")

    else:
        print("Wrong option!")