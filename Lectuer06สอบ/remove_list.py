fruita_with_apple = ["banana", "orange", "apple", "grape"]
while "apple" in fruita_with_apple:
    fruita_with_apple.remove("apple") # remove คือการลบข้อมูลออกจาก list
print(f"Fruits without apple: {fruita_with_apple}") #ถ้าไม่อยากให้หายหมดให้ใช้ fruita_with_apple.remove("apple") 1 ครั้ง