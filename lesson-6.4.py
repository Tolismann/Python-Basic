# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).  А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, name, color, is_police=False, speed=20):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self):
        print(f'{self.name} повернула')

    def show_speed(self):
        print(f'Текущая скорость {self.name} = {self.speed}')


class TownCar(Car):
    def show_speed(self):
        print(f'Текущая скорость {self.name} = {self.speed}')
        if self.speed > 60:
            print(f'Превышение скорости')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'Текущая скорость {self.name} = {self.speed}')
        if self.speed > 40:
            print(f'Превышение скорости')


class PoilceCar(Car):
    pass


c1 = TownCar('Toyota', 'White', speed=59)
print()
print()
print(c1.name)
print(c1.color)
print(c1.speed)
print(c1.is_police)
print()
print()
c1.go()
c1.show_speed()
c1.turn()
c1.stop()
c2 = SportCar('Mazda', 'Red', speed=99)
c2.go()
c2.show_speed()
c2.turn()
c2.stop()
c3 = PoilceCar('Porsche', 'Black', speed=88, is_police=True)
c3.go()
c3.show_speed()
c3.turn()
c3.stop()
c4 = WorkCar('BMW', 'Blue', speed=45)
c4.go()
c4.show_speed()
c4.turn()
c4.stop()