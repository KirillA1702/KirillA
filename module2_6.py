goods = [
    [1],
    [2],
]
product_1 = dict.fromkeys(['Название', 'Цена', 'Колличество', 'Ед.измерения'])
product_1['Название'] = input('Введите название товара №1: ')
product_1['Цена'] = int(input('Введите цену товара №1: '))
product_1['Колличество'] = int(input('Введите колличество товара №1: '))
product_1['Ед.измерения'] = input('Введите единицу измерения товара №1: ')

product_2 = dict.fromkeys(['Название', 'Цена', 'Колличество', 'Ед.измерения'])
product_2['Название'] = input('Введите название товара №2: ')
product_2['Цена'] = int(input('Введите цену товара №2: '))
product_2['Колличество'] = int(input('Введите колличество товара №2: '))
product_2['Ед.измерения'] = input('Введите единицу измерения товара №2: ')

goods[0].append(product_1); goods[1].append(product_2)
goods[0] = tuple(goods[0]); goods[1] = tuple(goods[1])

print(goods)
print('-' * 50)

name = []; price = []; qt = []; unit = []
scan_goods = dict.fromkeys(['Название', 'Цена', 'Колличество', 'Ед.измерения'])
goods_1 = dict(goods[0][1]); goods_2 = dict(goods[1][1])
for k, v in goods_1.items():
    if k == 'Название':
        name.append(v)
for k, v in goods_1.items():
    if k == 'Цена':
        price.append(v)
for k, v in goods_1.items():
    if k == 'Колличество':
        qt.append(v)
for k, v in goods_1.items():
    if k == 'Ед.измерения':
        unit.append(v)
for k, v in goods_2.items():
    if k == 'Название':
        name.append(v)
for k, v in goods_2.items():
    if k == 'Цена':
        price.append(v)
for k, v in goods_2.items():
    if k == 'Колличество':
        qt.append(v)
for k, v in goods_2.items():
    if k == 'Ед.измерения':
        unit.append(v)
scan_goods['Название'], scan_goods['Цена'], scan_goods['Колличество'], scan_goods['Ед.измерения'] = name, price, qt, unit
print(scan_goods)






