def path(n, m):
    yield 1
    for num in range(m - 1, n*m, m - 1):
        start_interval = num % n + 1
        if start_interval == 1:
            return
        yield start_interval


n, m = map(int, input('Введите число элементов в массиве и длину обхода через пробел: ').split())

for elem in path(n, m):
    print(elem, end='')
