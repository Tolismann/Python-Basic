# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# решения через функцию "list"
season = ['Зима', 'Весна', 'Лето', 'Осень']
month = int(input('Введите число соответствующее месяцу: '))
if month == 1 or month == 2 or month == 12:
    print(season[0])
elif month == 3 or month == 4 or month == 5:
    print(season[1])
elif month == 6 or month == 7 or month == 8:
    print(season[2])
elif month == 9 or month == 10 or month == 11:
    print(season[3])
else:
    print('Введено не правильное число месяца')

# решения через функцию "dict"
season = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
month = int(input('Введите число соответствующее месяцу: '))
if month == 1 or month == 2 or month == 12:
    print(season.get(1))
elif month == 3 or month == 4 or month == 5:
    print(season.get(2))
elif month == 6 or month == 7 or month == 8:
    print(season.get(3))
elif month == 9 or month == 10 or month == 11:
    print(season.get(4))
else:
    print('Введено не правильное число месяца')