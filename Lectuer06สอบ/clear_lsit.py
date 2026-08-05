nested_for = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for sublist in nested_for:
    sublist.clear()  # Clear each sublist #คือการลบข้อมูลออกจาก list โดยใช้ clear() ซึ่งจะทำให้ list ว่างเปล่า
print(nested_for)  # Output: [[], [], []]