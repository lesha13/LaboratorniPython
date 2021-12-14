with open('zavd1') as f:
    summ = sum(map(lambda x: float(x), f.read().split('\n')))
    f.seek(0)
    num = len(list(map(lambda x: float(x), f.read().split('\n'))))
    print(f'Середнє арифметичне: {summ/num}')
