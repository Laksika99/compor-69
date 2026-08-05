def add (a,b):
    return a + b

def subtract (a,b):
    return a - b

def multiply (a,b):
    return a * b

def divide (a,b):
    if b == 0:
        return "Error: Division by zero"
    else:
        return a / b

import math_operations

resul_add = math_operations.add(10, 5)
result_subtract = math_operations.subtract(10, 5)
result_multiply = math_operations.multiply(10, 5)
result_divide = math_operations.divide(10, 5)

print("Addition:", result_add)
print("Subtraction:", result_subtract)
print("Multiplication:", result_multiply)
print("Division:", result_divide)