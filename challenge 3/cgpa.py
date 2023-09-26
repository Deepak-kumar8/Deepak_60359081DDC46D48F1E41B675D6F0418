class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Test the function with a list of student objects
if __name__ == "__main__":
    students = [
        Student("Alice", "A101", 3.8),
        Student("Bob", "B202", 3.9),
        Student("Charlie", "C303", 3.7),
        Student("David", "D404", 3.95),
        Student("Eve", "E505", 3.85),
    ]

    sorted_students = sort_students(students)

    print("Students sorted by CGPA (descending order):")
    for student in sorted_students:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
