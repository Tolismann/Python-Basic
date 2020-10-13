# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def my_func(**kwargs):
    print(kwargs)


my_func(name=input('Name: '), surname=input('Surname: '), year_of_birth=int(input('Year of birth: ')),
        city=input('City of residence: '), email=input('Email: '), phone=input('Phone: '))
