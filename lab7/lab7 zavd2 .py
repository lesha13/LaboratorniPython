import numpy as np
from math import cos, sin

i = int(input('Рядки: '))
j = int(input('Стовпці: '))

x = int(input('x: '))
m = [[0 for y in range(j)] for z in range(i)]

for y in range(i):
    for z in range(j):
        m[y][z] = y*(sin(y*z) + cos(z*x))

m = np.array(m)     # Для красоти
print(m)

