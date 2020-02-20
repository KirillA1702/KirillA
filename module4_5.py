from functools import reduce

array = [x for x in range(int(input('x: ')), int(input('y: ')))]
array[-1] += 1
def my_func(n1, n2):
    return n1 + n2

print('Результат вычисления произведения всех элементов списка: ', reduce(my_func, array))