import numpy as np
from random import randint

'''
 Дана цілочислова прямокутна матриця. 
 Визначити номера рядків і стовпців всіх сідлових точок матриці. 
 Матриця А має сідлову точку А0, 
 якщо Aij є мінімальним елементом в і-у рядку і максимальним в j-у стовпці
'''

i = int(input('Рядки: '))
j = int(input('Стовпці: '))

m = [[randint(-10, 10) for x in range(j)] for y in range(i)]
m = np.array(m)             # Для красоти
print(m)

m_transp = [[m[x][y] for x in range(i)] for y in range(j)]
print(np.array(m_transp))   # Для красоти

num = []

for x in range(i):
    for y in range(j):
        if m[x][y] == min(m[x]) and m_transp[y][x] == max(m_transp[y]):
            num.append(str(x)+str(y))
print(num)
