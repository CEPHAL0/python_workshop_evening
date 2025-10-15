# Function with three parameters

def simple_interest_calculator(principal, time, rate):
    simple_interest = (principal * time * rate)/100
    amount = principal + simple_interest

    return simple_interest, amount

p = float(input("Enter the principal amount: "))
r = int(input("Enter the interest rate (0-100): "))
t = int(input("Enter the time in years: "))

# Calling Method 1
si, amt = simple_interest_calculator(principal=p, time=t, rate=r)

# Calling Method 2
si, amt = simple_interest_calculator(rate=r, principal=p, time=t)

# Calling Method 3
si, amt = simple_interest_calculator(p, t, r)


# Default Value for arguments
def simple_interest_calculator(principal, time=5, rate=13):
    simple_interest = (principal * time * rate) / 100
    amount = principal + simple_interest

    return simple_interest, amount

si, amt = simple_interest_calculator(principal=p, rate=r)

# Function Default Argument Rule
# Every argument on the right side of arguemnt with default value should also contain a default value

# For example
# def simple_interest_calculator(principal, time=5, rate): # Invalid
# def simple_interest_calculator(principal, time=5, rate=13): # Valid

# Percentage Calculator (Task)