from abc import ABC, abstractmethod
class Clothes(ABC):

    def __init__(self, size, height):
        self.size = size
        self.height = height

    @abstractmethod
    def coat(self):
        return self.size

    @abstractmethod
    def suit(self):
        return self.height

class Expense(Clothes):

    @property
    def coat(self):
        return round(self.size / 6.5 + 0.5, 2)

    @property
    def suit(self):
        return 2 * self.height + 0.3

    @property
    def all_expense(self):
        return round(self.suit + self.coat, 2)

ex = Expense(2, 2)
print(ex.suit)
print(ex.coat)
print(ex.all_expense)
