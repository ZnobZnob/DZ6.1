class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.aver_rate = float()

    def __str__(self):
        grades_count = 0
        for c in self.grades:
            grades_count += len(self.grades[c])
        self.aver_rate = round(sum(map(sum, self.grades.values())) / grades_count, 1)

        res = f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname} \n' \
              f'Средняя оценка за домашнее задание: {self.aver_rate} \n' \
              f'Курсы в процессе изучения: {self.courses_in_progress}\n' \
              f'Завершенные курсы: {self.finished_courses}'
        return res

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Ошибка')
            return
        return self.aver_rate < other.aver_rate


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.aver_rate = float()

    def __str__(self):
        grades_count = 0
        for c in self.grades:
            grades_count += len(self.grades[c])
        self.aver_rate = round(sum(map(sum, self.grades.values())) / grades_count, 1)
        res = f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname} \n' \
              f'Средняя оценка за лекцию: {self.aver_rate}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Ошибка')
            return
        return self.aver_rate < other.aver_rate


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname}'
        return res


# ------------------------------------------

student_1 = Student('Kurt', 'Cobain', 'M')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Java']
student_1.finished_courses += ['Git']

student_2 = Student('Sheldon', 'Cooper', 'M')
student_2.courses_in_progress += ['Git']
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['Python']

student_3 = Student('Leia', 'Organa', 'W')
student_3.courses_in_progress += ['Java']
student_3.finished_courses += ['Git']
student_3.finished_courses += ['Python']

# ------------------------------------------

lecturer_1 = Lecturer('Eddard ', 'Stark')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Git']
lecturer_1.courses_attached += ['Java']

lecturer_2 = Lecturer('Bilbo', 'Baggins')
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['Git']
lecturer_2.courses_attached += ['Java']

lecturer_3 = Lecturer('Tifa', 'Lockhart')
lecturer_3.courses_attached += ['Python']

# ------------------------------------------

reviewer_1 = Reviewer('Tom', 'Anderson')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Git']

reviewer_2 = Reviewer('Tyler', 'Durden')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Java']

# ------------------------------------------

student_1.rate_hw(lecturer_1, 'Python', 10)
student_1.rate_hw(lecturer_1, 'Python', 9)
student_1.rate_hw(lecturer_1, 'Git', 8)
student_1.rate_hw(lecturer_1, 'Git', 8)
student_1.rate_hw(lecturer_1, 'Java', 7)
student_1.rate_hw(lecturer_1, 'Java', 9)

student_1.rate_hw(lecturer_2, 'Python', 10)
student_1.rate_hw(lecturer_2, 'Python', 10)
student_1.rate_hw(lecturer_2, 'Git', 6)
student_1.rate_hw(lecturer_2, 'Git', 7)
student_1.rate_hw(lecturer_2, 'Java', 8)
student_1.rate_hw(lecturer_2, 'Java', 10)

student_1.rate_hw(lecturer_3, 'Python', 7)
student_1.rate_hw(lecturer_3, 'Python', 9)

student_2.rate_hw(lecturer_1, 'Python', 7)
student_2.rate_hw(lecturer_1, 'Python', 9)
student_2.rate_hw(lecturer_1, 'Git', 10)
student_2.rate_hw(lecturer_1, 'Git', 8)
student_2.rate_hw(lecturer_1, 'Java', 9)
student_2.rate_hw(lecturer_1, 'Java', 9)

student_2.rate_hw(lecturer_2, 'Python', 8)
student_2.rate_hw(lecturer_2, 'Python', 10)
student_2.rate_hw(lecturer_2, 'Git', 8)
student_2.rate_hw(lecturer_2, 'Git', 7)
student_2.rate_hw(lecturer_2, 'Java', 8)
student_2.rate_hw(lecturer_2, 'Java', 9)

student_2.rate_hw(lecturer_3, 'Python', 10)
student_2.rate_hw(lecturer_3, 'Python', 9)

student_3.rate_hw(lecturer_1, 'Python', 10)
student_3.rate_hw(lecturer_1, 'Python', 10)
student_3.rate_hw(lecturer_1, 'Git', 10)
student_3.rate_hw(lecturer_1, 'Git', 10)
student_3.rate_hw(lecturer_1, 'Java', 10)
student_3.rate_hw(lecturer_1, 'Java', 10)

student_3.rate_hw(lecturer_2, 'Python', 9)
student_3.rate_hw(lecturer_2, 'Python', 9)
student_3.rate_hw(lecturer_2, 'Git', 9)
student_3.rate_hw(lecturer_2, 'Git', 9)
student_3.rate_hw(lecturer_2, 'Java', 9)
student_3.rate_hw(lecturer_2, 'Java', 10)

student_3.rate_hw(lecturer_3, 'Python', 10)
student_3.rate_hw(lecturer_3, 'Python', 10)

# ------------------------------------------

reviewer_1.rate_hw(student_1, 'Python', 7)
reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_1, 'Java', 9)
reviewer_1.rate_hw(student_1, 'Java', 9)
reviewer_1.rate_hw(student_1, 'Git', 10)
reviewer_1.rate_hw(student_1, 'Git', 8)

reviewer_1.rate_hw(student_2, 'Python', 8)
reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Java', 10)
reviewer_1.rate_hw(student_2, 'Java', 9)
reviewer_1.rate_hw(student_2, 'Git', 7)
reviewer_1.rate_hw(student_2, 'Git', 6)

reviewer_1.rate_hw(student_3, 'Python', 10)
reviewer_1.rate_hw(student_3, 'Python', 8)
reviewer_1.rate_hw(student_3, 'Java', 7)
reviewer_1.rate_hw(student_3, 'Java', 7)
reviewer_1.rate_hw(student_3, 'Git', 8)
reviewer_1.rate_hw(student_3, 'Git', 8)

reviewer_2.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_1, 'Java', 7)
reviewer_2.rate_hw(student_1, 'Java', 9)
reviewer_2.rate_hw(student_1, 'Git', 6)
reviewer_2.rate_hw(student_1, 'Git', 8)

reviewer_2.rate_hw(student_2, 'Python', 7)
reviewer_2.rate_hw(student_2, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Java', 5)
reviewer_2.rate_hw(student_2, 'Java', 9)
reviewer_2.rate_hw(student_2, 'Git', 8)
reviewer_2.rate_hw(student_2, 'Git', 6)

reviewer_2.rate_hw(student_3, 'Python', 10)
reviewer_2.rate_hw(student_3, 'Python', 10)
reviewer_2.rate_hw(student_3, 'Java', 8)
reviewer_2.rate_hw(student_3, 'Java', 8)
reviewer_2.rate_hw(student_3, 'Git', 6)
reviewer_2.rate_hw(student_3, 'Git', 6)

# ------------------------------------------

student_list = [student_1, student_2, student_3]

lecturer_list = [lecturer_1, lecturer_2, lecturer_3]


def student_rating(student_list, course_name):
    sum_all = 0
    count_all = 0
    for stud in student_list:
        if stud.courses_in_progress == [course_name]:
            sum_all += stud.aver_rate
            count_all += 1
    aver_for_all = sum_all / count_all
    return aver_for_all


def lecturer_rating(lecturer_list, course_name):
    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            sum_all += lect.aver_rate
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all



print(f'Студенты:\n\n{student_1}\n\n{student_2}\n\n{student_3}\n')

print(f'Лекторы:\n\n{lecturer_1}\n\n{lecturer_2}\n\n{lecturer_3}\n')

print(f'Сравнение студентов по средним оценкам:\n\n'
      f'Студент 1 и Студент 2:{student_1 > student_2}\n'
      f'Студент 1 и Студент 3:{student_1 > student_3}\n'
      f'Студент 2 и Студент 3:{student_2 > student_3}\n')
print(f'Сравнение лекторов по средним оценкам:\n\n'
      f'Лектор 1 и Лектор 2:{lecturer_1 > lecturer_2}\n'
      f'Лектор 1 и Лектор 3:{lecturer_1 > lecturer_3}\n'
      f'Лектор 2 и Лектор 3:{lecturer_2 > lecturer_3}\n')

print(f"Средняя оценка студентов по курсу {'Java'}: {student_rating(student_list, 'Java')}")
print(f"Средняя оценка лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}")
