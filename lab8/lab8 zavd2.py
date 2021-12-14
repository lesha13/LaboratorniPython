from random import randint

n = int(input())
A = [randint(-10, 10) for el1 in range(n)]
B = [randint(-10, 10) for el2 in range(n)]
C = [randint(-10, 10) for el3 in range(n)]


def count_paralel(a, b):
    count = 0
    try:
        for i in range(1, len(a)):
            for j in range(1, len(a)):
                if i != j and a[i]/a[j] == b[i]/b[j]:
                    count += 1
    except ZeroDivisionError:
        pass
    return count


print(A)
print(B)
print(f'The number of paralel lines: {count_paralel(A, B)})
