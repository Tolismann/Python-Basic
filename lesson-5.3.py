# Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
employee = {}
sum_salary = 0
with open('text3.txt') as f_obj:
    for line in f_obj:
        surname, salary = line.split()
        employee[surname] = {'salary': float(salary)}
for line in employee:
    sum_salary += employee[line]['salary']
    average_salary = sum_salary / len(employee)
print(f'Cредняя величина дохода сотрудников = {average_salary}')
for line in employee:
    if employee[line]['salary'] < 20000:
        print(f'У сотрудника {line} оклад менее 20000')