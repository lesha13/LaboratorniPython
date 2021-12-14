with open('zavd2') as f:
    print(max(filter(lambda x: x < 0, map(lambda y: float(y), f.read().split('\n')))))
    f.seek(0)
    numbers = filter(lambda x: x < 0, map(lambda y: float(y), f.read().split('\n')))
    with open('V.dat', 'w') as f2:
        for z in numbers:
            f2.write(str(z) + '\n')
