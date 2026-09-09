try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"Error: Division by zero is not allowed. Details: {e}")

print("Program continues to run after handling the exception.")