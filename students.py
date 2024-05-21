# -*- coding: utf-8 -*-
"""Students.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18lA2Bf1vkK2obd_BclVSRSE53Kf0Qm8-
"""

class Student:
    def __init__(self, name, age, subjects):
        self.name = name
        self.age = age
        self.subjects = subjects

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Subjects: {', '.join(self.subjects)}"


class School:
    def __init__(self):
        self.students = []
        self.teachers = []

    def add_student(self, name, age, subjects):
        new_student = Student(name, age, subjects)
        self.students.append(new_student)

    def print_students(self):
        for student in self.students:
            print(student)

    def calculate_average_age(self):
        if not self.students:
            return 0
        total_age = sum(student.age for student in self.students)
        return total_age / len(self.students)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def print_teachers(self):
        for teacher in self.teachers:
            print(teacher)


if __name__ == "__main__":
    school = School()

    # Adding students
    school.add_student("Alice", 14, ["Math", "Science", "History"])
    school.add_student("Bob", 15, ["English", "Art", "Geography"])
    school.add_student("Charlie", 14, ["Math", "Science", "Physical Education"])

    # Printing student details
    print("Student Details:")
    school.print_students()

    # Calculating average age
    average_age = school.calculate_average_age()
    print(f"\nAverage Age of Students: {average_age:.2f}")