def my_div(x, y):
    try:
        return x / y
    except ZeroDivisionError:
            print(int(input('Вы ввели число <= 0! Введите значение Y > 0: ')))

my_div(x = int(input('Введите значение Х: ')),
       y = int(input('Введите значение Y: ')))