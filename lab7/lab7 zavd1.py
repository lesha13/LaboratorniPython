import numpy as np
from random import randint

'''
Визначити суму додатних елементів матриці з непарною сумою індексів
'''

i = int(input('Рядки: '))
j = int(input('Стовпці: '))

m = [[randint(-10, 10) for x in range(j)] for y in range(i)]
m = np.array(m)     # Для красоти
print(m)

sum_m = 0
for x in range(i):
    for y in range(j):
        if (x+y) % 2 != 0:      # непарність індекса
            if m[x][y] > 0:     # додатність числа
                sum_m += m[x][y]
print(sum_m)
