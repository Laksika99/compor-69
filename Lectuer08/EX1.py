# Read data from file and display it

file = open("employee.txt", "r")

for line in file:
    name, emp_id, dept = line.strip().split(",")

    print("Name:", name)
    print("ID:", emp_id)
    print("Dept:", dept)
    print()

file.close()