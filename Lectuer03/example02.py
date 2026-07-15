hours_worked = int(input("Enter the number of hours worked: "))
pay_rate = float(input("Enter the pay rate: "))
if hours_worked <= 40:
    gross_pay = hours_worked * pay_rate
else:
    overtime_hours = hours_worked - 40
    gross_pay = (40 * pay_rate) + (overtime_hours * pay_rate * 1.5)
print(f"The gross pay is: ${gross_pay:.2f}")