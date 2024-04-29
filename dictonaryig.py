students = {
    101: ("Alice", 85),
    102: ("Bob", 78),
    103: ("Charlie", 92),
    104: ("David", 80),
    105: ("Eva", 88)
}
sorted_students = sorted(students.items())
print("Sorted Student Information:")
for roll, (name, marks) in sorted_students:
    print(f"Roll Number: {roll}, Name: {name}, Marks: {marks}")
# Follow @codedepth for more!
