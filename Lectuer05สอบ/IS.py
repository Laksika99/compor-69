def is_armstrong(number):
    num_str = str(number)
    power = len(num_str)

    total = 0

    for i in num_str:
        total += int(i) ** power
    return total == number

print(is_armstrong(153))  # Output: True
print(is_armstrong(9474))  # Output: False   
print(is_armstrong(123))  # Output: True