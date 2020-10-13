# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
#
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

# вариант 1
def my_func(x, y):
    return x ** y
print(my_func(5.5, -5))

# вариант 2
def x_exponent_y(float_x, negative_int_y):
    if (isinstance(float_x, float)) and (isinstance(negative_int_y, int)):
        if (float_x > 0) and (negative_int_y < 0):
            result = 1
            for i in range(0, abs(negative_int_y)):
                result = result * (1/float_x)
            return result
    else:
        return None


r = x_exponent_y(5.5, -5)
print(r)