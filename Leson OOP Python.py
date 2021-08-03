class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def middle_grade(self):
        if self.grades == {}:
            return "Нельзя оценить!"
        else:
            all_grade = []
            for i in self.grades.values():
                all_grade += i
                return round(sum(all_grade) / len(all_grade), 1)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Ошибка!')
            return
        return self.middle_grade() < other.middle_grade()

    def __str__(self):
        print(f"Имя: {self.name}")
        print(f"Фамилия: {self.surname}")
        print(f"Средняя оценка за лекции: {self.middle_grade}")
        return


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        print(f'Имя проверяющего = {self.name}')
        print(f'Фамилия проверяющего = {self.surname}')
        return


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def middle_grade(self):
        if self.grades == {}:
            print("Нельзя оценить!")
        else:
            all_grade = []
            for i in self.grades.values():
                all_grade += i
                return round(sum(all_grade) / len(all_grade), 1)

    def __str__(self):
        print(f'Имя студента = {self.name}')
        print(f'Фамилия студента = {self.surname}')
        print(f'Средняя оценка за домашнее задание = {self.middle_grade()}')
        print(f'Курсы в процессе изучения: {self.courses_in_progress}')
        print(f'Завершенные курсы:{self.finished_courses}')
        return

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Ошибка!')
            return
        return self.middle_grade() < other.middle_grade()


some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses += ['Введение в программирование']

other_student = Student('Good', 'Win', 'your_gender')
other_student.courses_in_progress += ['Python']
some_student.finished_courses += ['Введение в программирование']

some_reviewer = Reviewer('Oleg', 'Bulygin')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Git']
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Python', 8)
some_reviewer.rate_hw(some_student, 'Git', 5)
some_reviewer.rate_hw(other_student, 'Python', 10)
some_reviewer.rate_hw(other_student, 'Python', 7)

other_reviewer = Reviewer('Denis', 'Rudakov')
other_reviewer.courses_attached += ['Git']
other_reviewer.rate_hw(some_student, 'Git', 7)

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']
some_student.rate_hw(some_lecturer, 'Python', 10)
some_student.rate_hw(some_lecturer, 'Python', 9)

other_lecturer = Lecturer('Elena', 'Nikitina')
other_lecturer.courses_attached += ['Python']
some_student.rate_hw(other_lecturer, 'Python', 1)
some_student.rate_hw(other_lecturer, 'Python', 2)
some_student.rate_hw(other_lecturer, 'Python', 7)
some_student.rate_hw(other_lecturer, 'Python', 9)
other_lecturer.courses_attached += ['Git']
some_student.rate_hw(other_lecturer, 'Git', 3)
some_student.rate_hw(other_lecturer, 'Git', 4)

print(some_lecturer)
print(f'Оценки лектору выставлены: {some_lecturer.grades}')
print()
print(other_lecturer)
print(f'Оценки другому лектору выставлены: {other_lecturer.grades}')
print()
print(some_reviewer)
print(f'Курс проверяющего: {some_reviewer.courses_attached}')
print()
print(other_reviewer)
print(f'Курс проверяющего: {other_reviewer.courses_attached}')
print()
print(some_student)
print(f'Оценки студенту выставлены: {some_student.grades}')
print()
print(other_student)
print(f'Оценки другому студенту выставлены: {other_student.grades}')
print()
print(f'Средний балл some студента меньше other студента? {some_student < other_student}')
print(f'Средний балл some лектора меньше other лектора? {some_lecturer < other_lecturer}')
print()

students_list = []
students_list += [some_student]
students_list += [other_student]

lecturers_list = []
lecturers_list += [some_lecturer]
lecturers_list += [other_lecturer]


def middle_grade_students(students_list, course):
    course = course.capitalize()
    grades_all = 0
    sum_all = 0
    for student in students_list:
        if course in student.grades.keys():
            print(f'Оценки студента {student.name} по курсу {student.grades[course]}')
            result = 0
            numbers = 0
            for i in student.grades[course]:
                result += i
                numbers += 1
            sum_numbers = result / numbers
            print(f'Средняя оценка {round(sum_numbers, 2)}')
            grades_all += sum_numbers
            sum_all += 1
    return grades_all / sum_all


course = input("Для расчета средней оценки студентов по курсу, введите название курса: ")
print(f'Средняя оценка студентов по курсу {course} {round(middle_grade_students(students_list, course), 2)}')

def middle_grade_lecturer(lecturers_list, course):
    course = course.capitalize()
    grades_all = 0
    sum_all = 0
    for lecturer in lecturers_list:
        if course in lecturer.grades.keys():
            print(f'Оценки студента {lecturer.name} по курсу {lecturer.grades[course]}')
            result = 0
            numbers = 0
            for i in lecturer.grades[course]:
                result += i
                numbers += 1
            sum_numbers = result / numbers
            print(f'Средняя оценка {round(sum_numbers, 2)}')
            grades_all += sum_numbers
            sum_all += 1
    return grades_all / sum_all


course = input("Для расчета средней оценки студентов по курсу, введите название курса: ")
print(f'Средняя оценка студентов по курсу {course} {round(middle_grade_lecturer(lecturers_list, course), 2)}')
