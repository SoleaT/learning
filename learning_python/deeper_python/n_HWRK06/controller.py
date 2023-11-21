from iomod import read_number
from games import *


def starting():
    while True:
        print('''Что выбрать?
        1. Угадывание числа
        2. Загадки
        3. Проверка даты
        4. Задача про ферзей''')
        n = read_number(input())
        match n:
            case 1:
                right_boundary = read_number(input('Правая граница: '))
                left_boundary = read_number(input('Левая граница: '))
                attempts = read_number(input('К-во попыток: '))
                if hit_digit(right_boundary, left_boundary, attempts):
                    print('Число угадано')
                else:
                    print('Число попыток исчерпано')
            case 2:
                loop_riddles()
                print_stat()
            case 3:
                # s = input('Введите дату в формате DD.MM.YYYY: ')
                s = '10.11.1700'
                print('Дата существует' if str_to_date(s) else 'Дата не существует')
            case 4:
                print('''
                Есть 2 варианта решения задачи:
                1. Поиск такого размещения ферзей, чтобы они не били друг другa.
                2. Рандомное размещение ферзей и проверка, бьют ли они друг друга''')
                m = read_number(input('Какой вариант выбрать? '))
                if 2 < m < 1:
                    print('Вы зафейлили задачу, я обиделся, прощайте!')
                    break
                if m == 1:
                    auto_solve()
                    draw_table()
                else:
                    generate_random_positions()
                    draw_table()
                    print('Бьют' if check_crossing() else 'Не бьют')
            case _:
                print('Выход из программы')
                break
