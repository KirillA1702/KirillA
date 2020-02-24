'''Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
сообщение и завершать скрипт.'''

from time import sleep
from itertools import cycle


class TrafficLight:

    def __init__(self):
        self.__color = 'Start'

    def running(self):
        count = 0
        for i in cycle(self.__color):
            print('Red')
            sleep(7.0)
            print('Yellow')
            sleep(2.5)
            print('Green')
            sleep(1.0)
            count += 1
            if count > 2:
                break

tl = TrafficLight()
tl.running()
