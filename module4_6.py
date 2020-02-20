from itertools import cycle, count

x = int(input('x: ')); y = int(input('y: ')); arr = []
for x in count(x):
    arr.append(x)
    if x >= y: break

print(tuple(arr))  # чтоб список чисел был в одну строку.

c = 0; n_count = int(input('Введите колличество итераций: '))
for num, x in enumerate(cycle(arr)):
    c += 1
    print(dict(Итерации = num + 1, Значение = x))
    if c >= n_count:
        break