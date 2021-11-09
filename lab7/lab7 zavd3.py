import numpy as np
from random import randint

i = int(input('Рядки: '))
j = 1    # бо вектор має 1 рядок

A = [[randint(-10, 10) for x in range(j)] for y in range(i)]
A = np.array(A)     # Для красоти
print(f'A:\n{A}')
b = [randint(-10, 10) for z in range(i)]
b = np.array(b)     # Для красоти
print(f'b:\n{b}')

m = []
for x in A:
    m.append(x * b)
m = np.array(m)     # Для красоти
print(f'm = A * b:\n{m}')

