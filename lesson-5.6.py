# Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет
# и наличие лекционных, практических
# и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета
# и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
#                           Физика:   30(л)   —   10(лаб)
#                      Физкультура:   —   30(пр)   —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
subjects = {}
count = 0
def get_int(count:str):
    if count == '-' or count == '':
        return 0
    index = count.find('(')
    return int(count[:index])
# print(get_int('100(л)'))
with open('text6.txt') as f_obj:
    for line in f_obj:
        subject, lecture, practice, laboratory = line.split()
        subjects[subject] = {'lecture': get_int(lecture), 'practice': get_int(practice), 'laboratory': get_int(laboratory)}
for line in subjects:
    sum_subject = subjects[line]['lecture'] + subjects[line]['practice'] + subjects[line]['laboratory']
    print(f'{line} {sum_subject}')

