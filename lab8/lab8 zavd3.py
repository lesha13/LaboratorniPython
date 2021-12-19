from random import randint


def x(n):
    if n == 0:
        return 0
    elif n == 1:
        return 9
    elif n > 1:
        return 2 * x(n-1) + 3 * x(n-2)


n = randint(0, 10)
print(f'result = {x(n)}')
