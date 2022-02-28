# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, param1=float, param2=float):
        self.param1 = param1
        self.param2 = param2

    @property
    def calculate(self):
        return f"Общий расход ткани {(self.param1 / 6.5 + 0.5) + (2 * self.param2 + 0.3)} "


class Coat(Clothes):
    def __init__(self, param=float):
        self.param = param
    def calculate(self):
        return f"Расход ткани на пальто {self.param / 6.5 + 0.5} метров"


class Dress(Clothes):
    def __init__(self, param=float):
        self.param = param
    def calculate(self):
        return f"Расход ткани на костюм {2 * self.param + 0.3} метров"


coat = Coat(46)
print(coat.calculate())

dress = Dress(1.64)
print(dress.calculate())

clothes = Clothes(46, 1.8)
print(clothes.calculate)
