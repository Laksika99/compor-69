student = {"name" : "Alice", "age": 25, "grade": "A"}

student["age"] = 26
student["major"] = "Computer Science"
print["major"] = "Computer Science"
print(student)

del student["grade"]
print(student)

removed_major = student.pop("major")
print(removed_major)
print(student)