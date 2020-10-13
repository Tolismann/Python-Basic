# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

rus_words = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('text4.txt') as f_obj:
    for el in f_obj:
        el = el.split(' ', 1)
        new_file.append(rus_words[el[0]] + ' ' + el[1])
    print(new_file)
with open('text4.1.txt', 'w') as f_obj:
    f_obj.writelines(new_file)