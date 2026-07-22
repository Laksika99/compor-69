input_string = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = ""

for char in input_string:
    upper_char = char.upper()
    if upper_char in vowels:
        vowel_count += "*"
    else:
        vowel_count += char
print("Modified string:", vowel_count)