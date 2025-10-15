# Return in functions
def sum(a, b):
    final_sum = a + b

    # pass the output to the user back
    return final_sum

# Function Call with return
output = sum(10, 20)

def square_root(a):
    return a ** (1/2)

output_2 = square_root(output)

print(f"The sum of 10 and 20 is {output} and the square root of {output} is {output_2}")

# Functions with multiple returns
def interest_calculator(principal, time, rate):
    simple_interest = (principal * time * rate)/100
    amount = simple_interest + principal

    # Multiple Return Values
    return simple_interest, amount

# Catch the multiple return values in multiple variables
si, amt = interest_calculator(10000, 20, 10)

print(f"The simple interest is {si} and the final amount is {amt}")
