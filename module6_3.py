'''Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров)'''

class Worker():
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {}

    def set_income(self, wage, bonus):
        self._income['wage'] = wage
        self._income['bonus'] = bonus

    def get_income(self):
        return self._income

class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(round(sum(self.get_income().values())))

worker_1 = Position('John', 'Smith', 'Director')
worker_1.get_full_name()
print(worker_1.position)
worker_1.set_income(11524.23, 5541.15)
worker_1.get_total_income()

