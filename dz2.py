salary = float(input("Enter your monthly salary: "))
bank_payment = float(input("Enter your monthly bank credit payment: "))
kom = float(input("Enter your communal services debt: "))

left = salary - (bank_payment + kom)
print(f"You have {left} dollars left after all payments this month")