# income -> float

income = float(input("What is your income?"))

if income <= 85528.0:
    tax = income * 0.18 - 556.2
else:
    surplus = income - 85528.0
    tax = 14839.2 + surplus * 0.32

if tax < 0.0:
    tax = 0.0
else:
    tax = round(tax,0)

print("Your Personal Income Tax (PIT) is:", tax)
