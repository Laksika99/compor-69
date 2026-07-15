inchar = input("Enter a character: ")
if inchar >= 'A' and inchar <= 'Z':
    print("You is an uppercase letter." , inchar)
elif inchar >= 'a' and inchar <= 'z':
    print("You is a lowercase letter." , inchar)
elif inchar >= '0' and inchar <= '9':
    print("You is put num" , inchar)
else:
    print("It's not a special character." , inchar)
