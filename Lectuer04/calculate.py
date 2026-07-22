keep_going = 'y'
while keep_going == 'y':
    sales = float(input("Enter sales amount: "))
    comm_rate = float(input("Enter commission rate : "))
    commi = sales * comm_rate
    print(f"The commission is ${commi :.2}.")
    keep_going = input('Do you want to calculate another ' +\
                       'commission? (y/n): ')