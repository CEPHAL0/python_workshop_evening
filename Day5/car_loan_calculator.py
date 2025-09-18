initial_price = 6500000
tenure_in_months = 60

downpayment = float(input("Enter how much % you want to put as down payment: "))

if downpayment > 50:
    interest = 13
elif downpayment > 40:
    interest = 15
elif downpayment > 30:
    interest = 16
else:
    interest = 20

paid_amount = (downpayment/100) * initial_price

remaining_amount = initial_price - paid_amount

interest_amount = (remaining_amount * (tenure_in_months/12) * interest)/100

total_amount = remaining_amount + interest_amount

amount_monthly = total_amount / tenure_in_months

print(f"The initial price was Rs.{initial_price}, you applied downpayment of {downpayment}% which is Rs.{paid_amount}, now you have to pay total of Rs.{total_amount} and monthly payment will be Rs.{amount_monthly}")