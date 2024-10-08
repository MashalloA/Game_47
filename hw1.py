class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self, ):
        if self.is_married:
            married = "женат(замужем)"
        else:
            married = "не женат(замужем)"

        print(f"Имя: {self.full_name}\n"
              f"Возраст: {self.age}\n"
              f"статус: {married}")

class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks

    def average_marks(self):
        if not self.marks:
            return 0
        return sum(self.marks.values()) / len(self.marks)

class Teacher(Person):
    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience

    def base_salary(self):
        base_salary = 30000
        bonus = 0
        percentage = self.experience / 3
        if self.experience >= 3:
            bonus = (0.05 * percentage) * base_salary
        return f"Полная зарплата учителя {self.full_name} составляет:", base_salary + bonus


teacher = Teacher("Александр", 30, True, 12)
teacher.introduce_myself()
print(f"salary: {teacher.base_salary()}\n")

def create_students():
    students = [
        Student("Иван Иванов", 16, False, {"математика": 5, "физика": 4, "химия": 5}),
        Student("Мария Петрова", 17, False, {"математика": 4, "физика": 3, "химия": 4}),
        Student("Алексей Смирнов", 15, False, {"математика": 5, "физика": 5, "химия": 4}),
    ]
    return students

students1 = create_students()
for student in students1:
    student.introduce_myself()
    print(f"Оценки: {student.marks} \n"
          f"Средняя оценка: {student.average_marks()}\n")
