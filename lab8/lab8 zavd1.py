from math import sin, cos, factorial


def f(x):
    if x < 0:
        sum1 = 1
        for y in range(1, 9):
            sum1 += (x**y)/(factorial(y))
        return sum1
    elif 0 <= x <= 5:
        return 15 + cos(x)**3
    else:
        return min([1, 2 * sin(x)])


a = float(input('a: '))
b = float(input('b: '))

u = max(f(a), f(b)) + f(3)
print(f'result = {u}')
