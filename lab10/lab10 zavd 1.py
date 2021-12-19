<<<<<<< HEAD
class ArithmeticProgression:
    def __init__(self, a=0, d=0):
        if type(a) == int or type(a) == float and type(d) == int or type(d) == float:
            self.__a = a
            self.__d = d
        else:
            raise Exception('Wrong data')

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if isinstance(value, int) or isinstance(value, float):
            self.__a = value
        else:
            raise ValueError

    @property
    def d(self):
        return self.__d

    @d.setter
    def d(self, value):
        if isinstance(value, int) or isinstance(value, float):
            self.__d = value
        else:
            raise ValueError

    def find_n_element(self, n: int):
        return self.a + self.d * (n-1)

    def find_n_sum(self, n: int):
        return (self.a + self.find_n_element(n)) * (n/2)

    def __str__(self):
        return f'Attributes: {self.__dict__}'


ap = ArithmeticProgression(1, 2)
ap.a = 2
ap.d = 3
print(ap.find_n_element(3))
print(ap.find_n_sum(3))
print(ap)
=======
class ArithmeticProgression:
    def __init__(self, a=0, d=0):
        if type(a) == int or type(a) == float and type(d) == int or type(d) == float:
            self.__a = a
            self.__d = d
        else:
            raise Exception('Wrong data')

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if isinstance(value, int) or isinstance(value, float):
            self.__a = value
        else:
            raise ValueError

    @property
    def d(self):
        return self.__d

    @d.setter
    def d(self, value):
        if isinstance(value, int) or isinstance(value, float):
            self.__d = value
        else:
            raise ValueError

    def find_n_element(self, n: int):
        return self.a + self.d * (n-1)

    def find_n_sum(self, n: int):
        return (self.a + self.find_n_element(n)) * (n/2)

    def __str__(self):
        return f'Attributes: {self.__dict__}'


ap = ArithmeticProgression(1, 2)
ap.a = 2
ap.d = 3
print(ap.find_n_element(3))
print(ap.find_n_sum(3))
print(ap)
>>>>>>> 6f5b3d6b309291675d532587588ce2ca77b26ff3
