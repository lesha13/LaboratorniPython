<<<<<<< HEAD
with open('zavd1') as f:
    summ = sum(map(lambda x: float(x), f.read().split('\n')))
    f.seek(0)
    num = len(list(map(lambda x: float(x), f.read().split('\n'))))
    print(f'Середнє арифметичне: {summ/num}')
=======
with open('zavd1') as f:
    summ = sum(map(lambda x: float(x), f.read().split('\n')))
    f.seek(0)
    num = len(list(map(lambda x: float(x), f.read().split('\n'))))
    print(f'Середнє арифметичне: {summ/num}')
>>>>>>> 6f5b3d6b309291675d532587588ce2ca77b26ff3
