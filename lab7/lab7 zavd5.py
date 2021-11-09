import numpy as np
from random import randint

'''
Дана цілочислова прямокутна матриця. 
Визначити суму елементів в тих стовпцях, які містять хоча б один від’ємний елемент
'''

i = int(input('Рядки: '))
j = int(input('Стовпці: '))

m = [[randint(-10, 10) for x in range(j)] for y in range(i)]
m = np.array(m)                     # Для красоти
print(m)

m_reversed = [[m[x][y] for x in range(i)] for y in range(j)]
print(np.array(m_reversed))

sum_m = 0

for x in m_reversed:
    if sorted(x)[0] < 0:
        sum_m += sum(x)
        print(f'Сума елементів в стовпці {m_reversed.index(x)}, який містять хоча б один від’ємний елемент: {sum_m}')
    sum_m = 0
