#Задача 2. Студенты

class Student:
    def __init__(self, name, surname, group, grades):
        self.name = name
        self.surname = surname
        self.group = group
        self.grades = grades

    def get_average_grade(self):
        return sum(self.grades) / len(self.grades)


students = []

for i in range(10):
    surname, name = input("Введите ФИ студента: ").split()
    group = input("Введите номер группы: ")
    grades = []

    for j in range(5):
        grade = int(input(f"Введите оценку {j+1}: "))
        grades.append(grade)

    student = Student(name, surname, group, grades)
    students.append(student)

students_sorted = sorted(students, key=lambda x: x.get_average_grade(), reverse=True)

for student in students_sorted:
    print(f"{student.name}, группа {student.group}, средний балл {student.get_average_grade()}")
