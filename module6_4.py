'''Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.'''

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('car is going')

    def stop(self):
        print('car stop')

    def turn_left(self):
        print('Поворот налево.')

    def turn_right(self):
        print('Пворот направо.')

    def show_speed(self):
        return self.speed


class TownCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Превышение скорости!')
        else:
            print('Нормально едем!')

class SportCar(Car):

    def car_sound(self):
        print('Wrooooommm-wroommm')

    def show_speed(self):
        super().show_speed()
        if self.speed > 300:
            print('Hey guy! Stop it!')
        else:
            print('Нормально едем!')

class WorkCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Превышение скорости')
        else:
            print('Нормально едем!')

class PoliceCar(Car):

    def flasher(self):
        print('VIU-VIU')

t_car = TownCar(60, 'black', 'Infinity "Q50"', False)
t_car.go()
print(t_car.speed, t_car.name, t_car.color, t_car.is_police)
t_car.show_speed(); t_car.stop()
s_car = SportCar(speed=301, color='Red', name='Ferrari "Enzo"', is_police=False)
print(s_car.speed, s_car.name, s_car.color, s_car.is_police)
s_car.car_sound()
print(s_car.speed)
s_car.show_speed()
p_car = PoliceCar(speed=60, color='black and white', name='Chevrolet "Caprize"', is_police=True)
p_car.flasher()
p_car.turn_left()
w_car = WorkCar(speed=41, color="dark blue", name='Citroen "Berlingo"', is_police=False)
print(w_car.speed, w_car.name, w_car.color, w_car.is_police)
w_car.show_speed()
w_car.turn_right()
