# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

num = int(input('Введите число n: '))
num1 = num
num2 = int(str(num) * 2)
num3 = int(str(num) * 3)
print('Сумма n + nn + nnn =', num1 + num2 + num3)