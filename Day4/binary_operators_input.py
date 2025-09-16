number1 = int(input("Enter the number 1: "))
number2 = int(input("Enter the number 2: "))

number3 = number1 + number2
number4 = number1 - number2
number5 = number1 * number2
number6 = number1 / number2
number7 = number1 ** number2
number8 = number1 % number2

print(f"""
For the {number1} and {number2}:
-----------
Sum: {number3}
Difference: {number4}
Product: {number5}
Division: {number6}
Exponent: {number7}
Modulus Division: {number8}
""")