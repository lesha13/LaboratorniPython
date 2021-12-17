import pickle


class University:
    def __init__(self, name: str, address: str, faculty_num: int, accreditation: int, rating: int):
        self.name = name
        self.address = address
        self.faculty_num = faculty_num
        self.accreditation = accreditation
        self.rating = rating

    def __str__(self):
        return f'{self.name}'


class StudentsDovidnyk:
    def __init__(self, *args):
        self.universities = args

    @property
    def get_universities(self):
        return f'Universities: {list(map(lambda u : u.name, self.universities))}'

    def get_info(self):
        print(self.get_universities)
        for el in self.universities:
            if el.name == input('About which university you want to know? '):
                info = input('What exactly do you want to know?\naddress/faculty/accreditation/rating: ')
                if info == 'rating':
                    return el.rating
                elif info == 'address':
                    return el.address
                elif info == 'accreditation':
                    return el.accreditation
                elif info == 'faculty':
                    return el.faculty
                else:
                    raise Exception('No such info')
            else:
                raise Exception('There\'s no such university')


dovidnyk = StudentsDovidnyk(University('Aboba', '1', 5, 100, 100), University('Big Bob', '2', 6, 80, 80))

with open('pickled zavd3', 'w+b') as f:
    pickle.dump(dovidnyk, f)
