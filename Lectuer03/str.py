#Program to compare the strings "Hary" and "Hark"
#Define the strings
stringl = "Nary"
string2 = "Mark"

#Compare the strings for equality
if stringl == string2:
    print(f'"(stringl)" and "(string2)" are equal.')
else:
    print(f'"(stringl)" and "(string2)" are not equal.')
#Lexicographical comparison
if stringl < string2:
    print(f'"(stringl)" comes before "(string2)" inlexicographical order.')
elif stringl > string2:
    print(f'"(stringl)" comes after "(string2)" inlexicographical order. ')
#Case-insensitive comparison
if stringl.lower() == string2.lower():
    print(f'"{stringl}" and "{string2}" are equal when case is ignored.')
else:
    print(f'"{stringl}" and "{string2}" are not equal when case is ignored.')