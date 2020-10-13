# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(arg_1, arg_2, arg_3):
    if arg_1 <= arg_2 and arg_2 <= arg_3:
        return arg_2 + arg_3
    elif arg_1 > arg_2 and arg_2 < arg_3:
        return arg_1 + arg_3
    else:
        return arg_1 + arg_2


print(my_func(int(input('Введите первый аргумент: ')), int(input('Введите второй аргумент: ')),
              int(input('Введите третий аргумент: '))))
