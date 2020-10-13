# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

# my_lines = ['Строка1 слово1 слово3\n', 'Строка2 слово2\n', 'Строка3 слово3\n']
# with open('text2.txt', 'w+') as f_obj:
#     f_obj.writelines(my_lines)
with open('text2.txt') as f_obj:
    lines = 0
    words = 0
    for line in f_obj:
        lines += 1
        words = len(line.split())
        print(f'количество слов в строке = {words}')
    print(f'Количество строк = {lines}')