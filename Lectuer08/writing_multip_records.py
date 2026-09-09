import struct

num_records = int(input("Enter the number of records to write: "))

with open("records.bin", "wb") as file:
    for _ in range(num_records):
       
            id_num =int(input("Enter ID: ")),
            name = input("Enter name: ").encode(),
            age = int(input("Enter age: ")),
            salary = float(input("Enter salary: "))
        
            data = struct.pack('i20sif', id_num, name, age, salary)
            file.write(data)
print(f"{num_records} records written to records.bin")