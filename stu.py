class Student:
    def __init__(self, name, roll_number, age, grade):
        self.name = name
        self.roll_number = roll_number
        self.age = age
        self.grade = grade

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def accept_student(self):
        print("Enter student details:")
        name = input("Name: ")
        roll_number = input("Roll Number: ")
        age = input("Age: ")
        grade = input("Grade: ")

        student = Student(name, roll_number, age, grade)
        self.students.append(student)
        print("Student added successfully!")