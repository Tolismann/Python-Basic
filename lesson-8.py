# == Лото ==
# 
# Правила игры в лото.
# 
# Игра ведется с помощью спе циальных карточек, на которых отмечены числа,
# и фишек (бочонков) с цифрами.
# 
# Количество бочонков — 90 штук (с цифрами от 1 до 90).
# 
# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
# расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
# 
# --------------------------
#     9 43 62          74 90
#  2    27    75 78    82
#    41 56 63     76      86
# --------------------------
# 
# В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
# случайная карточка.
# 
# Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
# 
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
# Если игрок выбрал "зачеркнуть":
#     Если цифра есть на карточке - она зачеркивается и игра продолжается.
#     Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
#     Если цифра есть на карточке - игрок проигрывает и игра завершается.
#     Если цифры на карточке нет - игра продолжается.
# 
# Побеждает тот, кто первый закроет все числа на своей карточке.
# 
# Пример одного хода:
# 
# Новый бочонок: 70 (осталось 76)
# ------ Ваша карточка -----
#  6  7          49    57 58
#    14 26     -    78    85
# 23 33    38    48    71
# --------------------------
# -- Карточка компьютера ---
#  7 87     - 14    11
#       16 49    55 88    77
#    15 20     -       76  -
# --------------------------
# Зачеркнуть цифру? (y/n)

from time import time
from random import random, randrange
from copy import deepcopy


# карточка
class Card_and_Barrel:
    def __init__(self):
        '''Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр'''
        self.line = 3
        self.cells = 9
        self.list = []
        self.dict = {}
        self.barrel = []
        self.list_barrel = []
        self.player_1_list = []
        self.player_2_list = []

    def get_random_card(self, name_card):
        self.name_card = name_card
        self.dict[self.name_card] = [[], [], []]
        print(name_card)
        print('-' * 28)
        [self.get_number_line(self.dict[name_card][i]) for i in range(self.line)]
        print('-' * 28)

    def get_number_line(self, card):
        self.number_line = sorted([i for i in self.get_random_number()])
        cells = self.cells
        length = len(self.number_line)
        while (cells > length):
            if self.get_random_bool() and (length != 0):
                self.length_check(card)
                cells -= 1
                length -= 1
            else:
                card.append('   ')
                cells -= 1
        for i in range(length):
            self.length_check(card)
        self.print_line(card)
        self.list = []

    def print_line(self, card):
        string = ''
        for i in card:
            string += i
        print(string)

    def length_check(self, card):
        if len(str(self.number_line[0])) == 1:
            card.append(' ' + str(self.number_line[0]) + ' ')
        else:
            card.append(str(self.number_line[0]) + ' ')
        self.number_line.pop(0)

    def get_random_number(self):
        self.exception = []
        self.filter(self.exception, self.name_card)
        while len(self.list) < 5:
            n = randrange(1, 91)
            if n not in self.exception:
                self.list.append(n)
                self.exception.append(n)
                yield n

    def filter(self, list_, name_in_dict):
        for i in range(len(self.dict[name_in_dict])):
            for g in range(len(self.dict[name_in_dict][i])):
                try:
                    int(self.dict[name_in_dict][i][g])
                    list_.append(int(self.dict[name_in_dict][i][g]))
                except:
                    continue

    def get_random_bool(self):
        if random() > 0.5:
            return True
        else:
            return False


class Game(Card_and_Barrel):

    def __init__(self, player_1, player_2):
        super().__init__()
        self.player_1 = player_1
        self.player_2 = player_2
        self.game = True

    def start_game(self):
        game.get_random_card(self.player_1)
        game.get_random_card(self.player_2)
        self.filter(self.player_1_list, self.player_1)
        self.filter(self.player_2_list, self.player_2)
        print('Начало игры.')
        while (len(self.list_barrel) < 90) and (self.game):
            self.new_barrel()
            self.check_win()
            if self.game:
                self.print_card(self.player_1)
                self.print_card(self.player_2)
        print('Игра окончена!')

    def new_barrel(self):
        self.number = self.get_barrel()
        self.list_barrel = []
        self.check_player(self.player_1)
        self.check_computer(self.player_2)

    def check_player(self, name):
        self.answer = (input(f'Ход {name}\'a.\nЗачеркнуть цифру? (Y/N)')).upper()
        if self.answer == 'Y':
            a = []
            self.filter(a, name)
            if self.number in a:
                print('Правильно число есть на карточке.')
                self.template_replacement(name)
            else:
                print('Не правильно. Число есть на карточке.')
                return self.game_over(self.player_1, self.player_2)
        elif self.answer == 'N':
            a = []
            self.filter(a, self.player_1)
            if self.number not in a:
                print('Правильно. Числа нет на карточке.')
            else:
                print('Не правильно. Число есть на карте.')
                return self.game_over(self.player_1, self.player_2)
        else:
            self.check_player(name)

    def template_replacement(self, name):
        for i in range(len(self.dict[name])):
            for g in range(len(self.dict[name][i])):
                if (str(self.number) in self.dict[name][i][g]) and (self.number == int(self.dict[name][i][g])):
                    if (name == self.player_1):
                        self.player_1_list.remove(int(self.dict[name][i][g]))
                    elif (name == self.player_2):
                        self.player_2_list.remove(int(self.dict[name][i][g]))
                    self.dict[name][i][g] = (self.dict[name][i][g]).replace(self.dict[name][i][g], ' - ')
                    return

    def check_computer(self, name):
        if self.game:
            a = []
            self.filter(a, name)
            if self.number in a:
                self.template_replacement(name)
            else:
                pass
            print(f'{name} сделал ход.')

    def check_win(self):
        if (len(self.player_1_list) > 0) and (len(self.player_2_list) > 0):
            return
        elif (len(self.player_1_list) == 0) and (len(self.player_2_list) > 0):
            return self.game_over(self.player_2, self.player_1)
        elif (len(self.player_1_list) > 0) and (len(self.player_2_list) == 0):
            return self.game_over(self.player_1, self.player_2)
        else:
            self.game = False
            return print(f'Ничья!')

    def game_over(self, name_loser, name_winner):
        print(f'{name_loser} ты проиграл!\n{name_winner} выйграл!')
        self.game = False

    def get_barrel(self):
        while len(self.list_barrel) < 1:
            n = randrange(1, 91)
            if n not in self.barrel:
                self.list_barrel.append(n)
                self.barrel.append(deepcopy(n))
                print(f'Бочонок №{n} (осталось {90 - len(self.barrel)})')
                return n

    def print_card(self, name):
        string = ''
        for i in range(len(self.dict[name])):
            for g in range(len(self.dict[name][i])):
                string += self.dict[name][i][g]
            if i != 2:
                string += '\n'
        print(name)
        print('-' * 28)
        print(string)
        print('-' * 28)


game = Game('Player', 'Computer')
game.start_game()
