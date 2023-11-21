from itertools import combinations_with_replacement
from random import sample

__all__ = ['coords', 'generate_right_positions', 'draw_table', 'generate_random_positions',
           'check_crossing', 'auto_solve']
coords = []
count = 5  # >5 может считать ну очень долго. хотя и так зависает периодически :(
max_table = 8


def check_place(place: tuple) -> bool:  # проверка на пересечение по всем линиям атаки
    for i in range(len(coords)):
        if coords[i][0] == place[0] or coords[i][1] == place[1]:
            return False  # проверка прямой линии
    for n in range(len(coords)):
        i, j = 1, 1
        k = 0
        while k < max(max_table - place[0], max_table - place[1]):  # проверка диагоналей
            if place[0] - i >= 0 and place[1] - j >= 0:
                if coords[n][0] == place[0] - i and coords[n][1] == place[1] - j:
                    return False
            if place[0] - i >= 0 and place[1] + j <= max_table:
                if coords[n][0] == place[0] - i and coords[n][1] == place[1] + j:
                    return False
            if place[0] + i <= max_table and place[1] - j >= 0:
                if coords[n][0] == place[0] + i and coords[n][1] == place[1] - j:
                    return False
            if place[0] + i <= max_table and place[1] + j <= max_table:
                if coords[n][0] == place[0] + i and coords[n][1] == place[1] + j:
                    return False
            i += 1
            j += 1
            k += 1
    return True


def auto_solve():  # классик решение - само генерится, само проверяется
    coords.clear()
    for i in range(1, count + 1):
        coords.append(*generate_right_positions())  # получаем список кортежей
    print(coords)


def generate_right_positions():  # создание списка позиций для классик решения
    a = sample(list(combinations_with_replacement(range(1, max_table + 1), 2)), 1)  # да, спионерила идею
    if not coords:
        return a
    else:
        while not check_place(*a):
            a = sample(list(combinations_with_replacement(range(1, max_table + 1), 2)), 1)
        return a


def draw_table():  # рисование таблички
    table = [['▢' for _ in range(max_table)] for _ in range(max_table)]
    for coord in coords:
        table[coord[0] - 1][coord[1] - 1] = '▣'
    for i in table:
        print(*i, end='\n')


def generate_random_positions():  # просто нужное к-во позиций
    coords.clear()
    for _ in range(count):
        coords.append(*sample(list(combinations_with_replacement(range(1, max_table + 1), 2)), 1))


def check_crossing():  # проверка пересечений для рандом решения
    place = coords.pop(0)  # костыль конечно, но иначе пришлось бы переписывать всю функцию
    return False if check_place(place) else True


if __name__ == '__main__':
    auto_solve()
    draw_table()
    print('_' * 90)
    coords.clear()
    generate_random_positions()
    draw_table()
    print(check_crossing())
