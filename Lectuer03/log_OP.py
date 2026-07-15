age = int(input("Enter your age: "))
incom = float(input("Enter your income: "))
if age >= 18 and age <= 65 and incom >= 30000:
    print("You are eligible for the loan.")
else:
    print("You are not eligible for the loan.")