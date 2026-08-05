heroes = ['Iroon man ', 'Captain America', 'Thor', 'Hulk', 'Black Widow']
h2 = heroes.copy() #คือการคัดลอกข้อมูลจาก list หนึ่งไปยังอีก list หนึ่ง โดยใช้ copy()
print(h2) # Output: ['Iroon man ', 'Captain America', 'Thor', 'Hulk', 'Black Widow']

heroes.append('Hawkeye') #คือการเพิ่มข้อมูลเข้าไปใน list โดยใช้ append()
heroes.insert(2, h2[0]) #คือการเพิ่มข้อมูลเข้าไปใน list โดยใช้ insert() ซึ่งจะทำให้ข้อมูลที่เพิ่มเข้าไปอยู่ในตำแหน่งที่เรากำหนด
print(heroes.index('Thor')) # Output: 3 #คือการหาตำแหน่งของข้อมูลใน list โดยใช้ index()
heroes.sort() #คือการเรียงข้อมูลใน list โดยใช้ sort() ซึ่งจะทำให้ list เรียงจากน้อยไปมาก
print(heroes) # Output: ['Black Widow', 'Captain America', 'Hawkeye', 'Hulk', 'Iroon man ', 'Thor']
heroes.remove('Hulk') #คือการลบข้อมูลออกจาก list โดยใช้ remove() ซึ่งจะทำให้ข้อมูลที่เรากำหนดหายไปจาก list