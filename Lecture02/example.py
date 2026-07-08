weight = float(input("Enter your weight in kg: "))
hight = float(input("Enter your height in meters: "))
print(f"Your height is {hight } cm.")
print(f"Your weight is {weight} kg.")

BMI = weight / (hight/10 ** 2)
print("Your BMI is ", format(BMI,".2f"))
