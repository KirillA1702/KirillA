'''Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.'''

class Stationery:
    def __init__(self):
        self.title = 'Канцелярские пренадлежности.'

    def draw(self):
        print('Запуск отрисовки...')
        # return 'Запуск отрисовки...'  # вызов произойдет один раз, потом уникальные сообщения.

class Pen(Stationery):
    def draw(self):
        super().draw()
        print('Рисуем круг.')

class Pencil(Stationery):
    def draw(self):
        super().draw()
        print('Заштриховываем круг.')

class Handle(Stationery):
    def draw(self):
        super().draw()
        print('Дорисовываем лучи.')

s = Stationery()
print(s.title)
# print(s.draw())
p = Pen()
p.draw()
penc = Pencil()
penc.draw()
h = Handle()
h.draw()