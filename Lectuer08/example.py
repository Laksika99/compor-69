def example_w_plus_mode():
    with open("example.txt", "w+") as file:
        file.write("This line is written in w+ mode.\n")
        file.seek(0)  # Move the cursor to the beginning of the file
        file.write("This line is also written in w+ mode.\n")
        file.seek(0)  # Move the cursor to the beginning of the file
        content = file.read()
        print("content of the file:")
        print(content)