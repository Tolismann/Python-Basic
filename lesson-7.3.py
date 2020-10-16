# Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
# соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение
# и целочисленное (с округлением до целого) деление клеток, соответственно.
# Сложение. Объединение двух клеток.
# При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек
# двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется
# как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление
# количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.

class Cell:
    def __init__(self, cells1, cells2):
        self.cells1 = int(cells1)
        self.cells2 = int(cells2)

    def __add__(self, num1, num2):
        self.sum_cells = int(num1 + num2)

    def __sub__(self, num1, num2):
        if int(num1 - num2) > 0:
            self.dif_cells = int(num1 - num2)
        else:
            print('Разность отрицательна')
            self.dif_cells = None


    def __mul__(self, num1, num2):
        self.new_cells = int(num1 * num2)


    def __truediv__(self, num1, num2):
        self.div_cells = int(num1 % num2)

    # def make_order(self, number_of_cells):
    #     for i in range(int(self.cells1/self.cells2)):
    #         r = '*' * number_of_cells + '\n'
    #     r += "*" * (self.cells1 % number_of_cells)
    #     return r

c = Cell(5, 7)
print(c.cells1)
print(c.cells2)
c.__add__(c.cells1, c.cells2)
print(c.sum_cells)
c.__sub__(c.cells1, c.cells2)
print(c.dif_cells)
c.__mul__(c.cells1, c.cells2)
print(c.new_cells)
c.__truediv__(c.cells1, c.cells2)
print(c.div_cells)
