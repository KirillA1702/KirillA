from math import factorial as fact
n = int(input('Введите число n: '))
def generator(n):
    for x in range(1, n + 1):
        yield x
g = generator(n)
for n in g:
    print(fact(n))