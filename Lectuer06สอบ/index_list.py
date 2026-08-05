animals = ["cat", "dog", "rabbit", "hamster"]
#คือการลบข้อมูลออกจาก list โดยใช้ del
first_dog_index = animals.index("dog") # find the index of "dog" #ก็คือการหาตำแหน่งของข้อมูลใน list โดยใช้ index
print(f"The second animal in the list is: {animals[first_dog_index]}") # Output: dog #อันนี้เราสามารถใช้ del เพื่อทำการลบข้อมูลออกจาก list ได้ โดยเราสามารถระบุ index ของข้อมูลที่ต้องการลบได้