try:
    numerator = float(input("Enter the numerator:"))
    denominator = float(input("Enter the denominator"))

    result = numerator / denominator
    print(f"The result is : {result}")

except ZeroDivisionError:
    print("Error: Youcannot divide by zero. ")

except ValueError:
    print("Error: Invalid input. Please enter numeric values.") 

finally:
    print("Excution completed , whather an exception occurred or not.  ")
print("End of program")