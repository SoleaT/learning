from itertools import combinations
from pprint import pprint

from deeper_python.n_HWRK03.src.io import read_number


def init_task4():
    tour = {
        'Палатка': 20,
        'Чугунок': 3,
        'Кружка': 2,
        'Спальник': 7,
        'Еда': 5,
        'Поджопник': 1,
        'Аптечка': 1,
        'Топор': 4,
        'Байдарка': 8,
    }
    capacity = read_number(input('Введите вместимость рюкзака: '))
    backpack = []

    # один вариант
    # for key, item in sorted(tour.items(), key=lambda x: x[1], reverse=True):
    #     if capacity - item < 0:
    #         continue
    #     capacity -= item
    #     backpack.append(tuple([key, item]))
    # print('В рюкзак поместится (начиная с тяжёлого): ',*backpack)

    # много вариантов
    for k in tour.keys():
        c = 0
        one_variant = []
        for key, item in tour.items():
            if k == key: continue
            if c + item > capacity: continue
            c += item
            one_variant.append(tuple([key, item]))
        if one_variant not in backpack:
            backpack.append(one_variant)
    print('В рюкзак можно запихать: ')
    pprint(backpack, width=120)
    print('Выбирай мудро.')
    return

