import numpy as np
from math import cos, sin

i = int(input('Рядки: '))
j = int(input('Стовпці: '))

x = int(input('x: '))
m = [[0 for y in range(j)] for z in range(i)]

product = 1

for y in range(i):
    for z in range(j):
        m[y][z] = y*(sin(y*x) + cos(z*x))
        if y*z < x:
            product *= m[y][z]

m = np.array(m)     # Для красоти
print(m)
print(product)
