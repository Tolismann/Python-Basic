# Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

my_lines = []
while True:
    line = input('Введите данные: ')
    if line == '':
        print(my_lines)
        exit()
    else:
        n_line = line + '\n'
        my_lines.append(n_line)

    with open('text1.txt', 'w') as f:
        f.writelines(my_lines)