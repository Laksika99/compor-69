import struct
record = (1, 'JohnDoe', 20, 3.75)

with open("example.txt", "a") as file:
    file.write("This line is appended.\n")

    with open("record.bin", "wb") as file:
        data = struct.pack('i20sif', record[0], record[1].encode(), record[2], record[3])
        file.write(data)