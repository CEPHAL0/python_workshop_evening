# Function Signature
# What is the name of the function ?
# How many arguments are there in the function ?
# How many values are returned in the function ?

# 1. Function signature without parameters and returns
def simple_function():
    print("Hello from function")

# Calling the function
simple_function()


# 2. Function Signature with parameters but no return
def another_function(argument1):
    print(f"I have recieved the argument {argument1}")

# Calling the function
name = input("Enter the name: ")
another_function(argument1=name)


# 3. Function Signature with no parameters but return value
def function_with_no_arguments():
    return "Hello"

# Calling the function
output = function_with_no_arguments()
print(f"The output of the function is {output}")


# 4. Function Signature with parameters and returns
def interest_calculator(principal, time, rate):
    simple_interest = (principal * time * rate) / 100
    amount = simple_interest + principal

    # Multiple Return Values
    return simple_interest, amount


# Catch the multiple return values in multiple variables
si, amt = interest_calculator(10000, 20, 10)
print(f"The simple interest is {si} and the final amount is {amt}")