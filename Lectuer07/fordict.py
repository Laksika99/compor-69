phonebook = {'Anirach': '123-456-7890', 'Bob': '987-654-3210', 'Charlie': '555-555-5555'}

phonebook['Bart'] = [1, 3, 5]

elements = len(phonebook)
print('There are ', elements, ' names in phonebook')

for key in phonebook:
    print(key, 'phone number is: ', phonebook[key])

    phonebook['Bart'][1] = 9
    print(phonebook)