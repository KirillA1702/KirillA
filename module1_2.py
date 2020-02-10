time = int(input('Введите колличество секунд: '))
hour = time // (60 * 60)
min = time // 60; min = min % 60
sec = time % (60 * 60); sec = sec % 60
print(f'Точное время {hour} : {min} : {sec}')