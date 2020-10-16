# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes_ABC:
    @abstractmethod
    def __init__(self, sizeABC, heightABC):
        self.size = sizeABC
        self.height = heightABC

    @abstractmethod
    def get_tissue_consumption(self):
        pass


class Clothes(Clothes_ABC):
    def __init__(self, size, height):
        super().__init__(size, height)

    @property
    def get_tissue_consumption(self):
        for_coat = (int(self.size / 6.5) + 0.5)
        for_suit = (2 * self.height + 0.3)
        return f'Расход для пальто - {for_coat}\n' \
               f'Расход для костюма - {for_suit}'
c = Clothes(31, 24)
print(c.get_tissue_consumption)
