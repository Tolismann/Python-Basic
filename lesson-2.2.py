# Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

num_of_values = int(input('Введите необходимое колличество значений элементов: '))
values = []
val = 0
element = 0
while val < num_of_values:
    values.append(input('Введите следущее значение: '))
    val += 1
print(values)
for elem in range(int(len(values) / 2)):
    values[element], values[element + 1] = values[element + 1], values[element]
    element += 2
print(values)