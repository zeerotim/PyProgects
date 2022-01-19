"""
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
 одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм.
 У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
 V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: 4
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, attr: int): # attr = размер или рост
        self.attr = attr

    @abstractmethod
    def textile_consumption(self):
        return


class Coat(Clothes):
    # def __init__(self, attr):
    #     self.attr = attr

    @property
    def textile_consumption(self):
        return self.attr/6.5+0.5


class Suit(Clothes):
    # def __init__(self, attr):
    #     self.attr = attr

    @property
    def textile_consumption(self):
        return 2*self.attr+0.3


c = Coat(46)
s = Suit(180)

print(f"Расход ткани для пальто: {c.textile_consumption}")
print(f"Расход ткани для кастюма: {s.textile_consumption}")

