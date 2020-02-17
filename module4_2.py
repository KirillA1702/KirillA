import random

print('Введите диапазон сравниваемых чисел, где X - нижняя граница, а Y - верхняя.')
array = [x for x in range(int(input('x: ')), int(input('y: ')))]; random.shuffle(array); array_2 = []; i = 0
while i < len(array) - 1:
    tmp = array[i]; array[i] = array[i+1]
    if array[i] > tmp: array_2.append(array[i])
    i +=1

print('Исходный список: ', array); print('Результат: ', array_2)