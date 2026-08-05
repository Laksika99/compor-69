grades = [85, 92, 78, 96, 88]
third_grade = grades.pop(2) # remove the grade at index 2 (78) from the list
grades.append(third_grade) # append the popped grade back to the list
print(f"Grades after popping and appending: {grades}")  # Output: [85, 92, 96, 88, 78]