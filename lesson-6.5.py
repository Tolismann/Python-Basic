# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, name):
        self.title = name

    def draw(self):
        print('Запуск отрисовки')
        print()
        print()


class Pen(Stationery):
    def draw(self):
        print('Ручка')
        print('Запуск отрисовки')
        print(self.title + ' рисует')


class Pencil(Stationery):
    def draw(self):
        print('Карандаш')
        print('Запуск отрисовки')
        print(self.title + ' рисует')


class Handle(Stationery):
    def draw(self):
        print('Маркер')
        print('Запуск отрисовки')
        print(self.title + ' рисует')


p1 = Pen('Ручка')
p1.draw()
p2 = Pencil('Карандаш')
p2.draw()
p3 = Handle('Маркер')
p3.draw()