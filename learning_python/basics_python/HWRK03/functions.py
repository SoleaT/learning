from random import randint, random


def task1(sze=5):
    lst = [randint(1, 10 + 1) for _ in range(sze)]  # формируем список из рандомных значений от 1 до 10
    new_lst = []
    for i in range(
            sze // 2 if sze % 2 == 0 else sze // 2 + 1):  # к-во итераций цикла зависит от чётности размера списка
        new_lst.append(lst[i] * lst[sze - i - 1])  # формируем новый список
    print(lst, '->', new_lst)


def task2(sze=5):
    lst = [round(random() * 10, 2) for _ in range(sze)]          #формируем список из рандомных значений от 1 до 10
    print(lst)
    lst = [round(lst[i] - int(lst[i]), 2) for i in range(sze)]   #изменяем список, чтоб остались только дробные части
    print('Разница между максимальной и минимальной дробными частями =', max(lst) - min(lst)) #и можно было спокойно использовать min max


def task3(decnumber):
    dcnum = []
    while decnumber > 0:
        dcnum.append(decnumber % 2)
        decnumber //= 2
    print(dcnum[::-1])


def task4(lst, k=8):                            #список заполняется рекурсией
    cur_len = len(lst)                          #размер списка
    if cur_len >= k * 2:                        #берётся для проверки выхода из рекурсии
        return lst                              #выход

    lst.append(lst[cur_len - 1] + lst[cur_len - 2])      #в конец списка добавляем обычное число фибоначчи
    lst.insert(0, (-1) ** (cur_len // 2) * lst[cur_len]) #в начало - нега
    task4(lst, k)                                        #и поехали заново
    return lst
