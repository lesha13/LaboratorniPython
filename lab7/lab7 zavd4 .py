import numpy as np
from random import randint

'''
Розмістити елементи непарних рядків у порядку спадання
'''

i = int(input('Рядки і стовпці: '))
j = i

m = [[randint(-10, 10) for x in range(j)] for y in range(i)]
print(f'm default:\n{np.array(m)}')

for x in m:
    if m.index(x) % 2 != 0:
        m[m.index(x)] = sorted(x, reverse=True)
else:
    m = np.array(m)
print(f'm sorted:\n{m}')
