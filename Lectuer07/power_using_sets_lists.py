attendance_week = [
    ["Alice", "Bob", "Charlie", "David"],
    ["Alice", "Charlie", "David"],
    ["Alice", "Bob", "David"],
    ["Alice", "David", "Eve"],
    ["Bob", "Charlie", "David"]
]

attendance_set = [set(day) for day in attendance_week]
print(attendance_set)

attendance_set = [set(day) for day in attendance_week]
print(attendance_set)

attendance_set = [
    {"Alice", "Bob", "Charlie"},
    {"Alice", "David", "Charlie"},
    {"Bob", "David", "Eve"},
]

present_every_day = set.intersection(*attendance_set)
print("Present present every day:", present_every_day)

all_students = set.union(*attendance_set)
absent_at_least_one_day = all_students - present_every_day
print("Absent at least one day:", absent_at_least_one_day)

first_day_attendance = attendance_set[0]
last_day_attendance = attendance_set[-1]
first_day_but_not_last = list(first_day_attendance - last_day_attendance)
print("Present on first day but absent on last day:", first_day_but_not_last)

unique_students_count = len(all_students)
print("Total unique students:", unique_students_count)