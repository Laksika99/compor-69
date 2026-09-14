phonebook = {'Anirach': '123-456-7890', 'Bob': '987-654-3210', 'Charlie': '555-555-5555'}

print(phonebook)
print(phonebook['Bob'])
print(phonebook.get('Charlie'))

key = 'David'
if key in phonebook:
    print(phonebook['David'])
else:
    print(key + ' not in phonebook')

    phonebook['kevin'] = '111-222-3333'
    phonebook['David'] = '444-444-4444'
    phonebook['Bob'] = '999-999-9999'
    print(phonebook)

    del phonebook['kevin']
    print(phonebook)