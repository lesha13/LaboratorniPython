from datetime import date, datetime


def get_today_date():
    return date(datetime.today().year, datetime.today().month, datetime.today().day)


subjects = ['Programming', 'Math', 'Algorithms', 'Philosophy']
marks = [4, 5, 3, 2]


class Student:
    def __init__(self, name: str, birth_date: date, admission_date: date,
                 course: int, marks: list = None, studentship: int = 0):
        self.name = name
        self.birth_date = birth_date
        self.admission_date = admission_date
        self.course = course
        self.marks = marks
        self.studentship = studentship
        self.__end = date(self.admission_date.year + 4, 5, 31)
        self.__subjects_marks = {x: y for x in subjects for y in marks}

    def get_average_mark(self):
        return sum(self.marks) / len(self.marks)

    def get_lover_than_average(self):
        return [el for el in self.__subjects_marks.keys() if self.__subjects_marks[el] > self.get_average_mark()]

    def get_age(self):
        return f'The age is: {get_today_date().year - self.birth_date.year}'

    def get_graduation_day(self):
        return (f'Today is: {get_today_date()}\n'
                f'The university ends: {self.__end}\n'
                f'Theres {str(self.__end - get_today_date())[:-9:]} left')

    def __str__(self):
        return f'Student: {self.name}'


birth = date(2004, 8, 13)
admission = date(2021, 9, 1)
s = Student('Oleksii', birth, admission, 1, marks)
print(s.get_age())
print(s.get_graduation_day())
print(s.get_average_mark())
print(s.get_lover_than_average())
print(s)
