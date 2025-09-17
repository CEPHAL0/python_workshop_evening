price = int(input("Enter the price of item: "))

# Price greater than 1000
greater_than_1000 = price > 1000

if greater_than_1000:
    discount = 20
else:
    discount = 10

discount_price = (discount/100) * price

final_price = price - discount_price

print(f"The final price after the {discount}% is {final_price}")