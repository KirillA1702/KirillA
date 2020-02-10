earn = int(input('Введите значение выручки: '))
cost = int(input('Введите значение издержки: '))
staff = int(input('Введите колличество сотрудников фирмы: '))
if earn > cost:
    print('Ваша фирма работает в прибыл!')
    if (earn - cost) > 0:
        profit = round((((earn - cost) / earn) * 100), 1)
        print(f'Рентабельность составляет {profit} %')
elif earn < cost:
    print('Ваша фирма терпит убытки!')
else:
    print('Фух... Вы вышли в ноль!')
profit = round(((earn - cost) / staff), 2)
print(f'Прибыль на одного человека составляет {profit} у.е')