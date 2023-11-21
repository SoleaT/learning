from random import uniform, randint
from math import pi, floor
from decimal import Decimal, ROUND_FLOOR


def task1(d, fnumber):
    if d < 1:
        order, temp = 0, d
        while temp < 1:
            temp *= 10
            order += 1
        return floor(fnumber * (10 ** order)) * d
    else:
        return int(fnumber)  # я не помню, было ли в условии насчет точности 1 и выше, поэтому на всякий


def task1var(d, fnumber=str(pi)):  # только для чисел с точкой
    order = int(len(d) - d.find('.'))
    pref = fnumber.find('.')
    return fnumber[:pref] + '.' + fnumber[pref + 1:pref + order]


def task2():
    lst = [randint(0, 10) for _ in range(randint(3, 12))]
    print(lst)
    print(list(item for item in lst if lst.count(item) < 2))


def task3():
    k = randint(1, 7)  # выбираем сколько степеней.
    filestr = str(randint(0, 100)) + ' = 0'
    for i in range(1, k + 1):
        num = randint(0, 100)
        if num > 0:
            if i == 1:
                filestr = f'{num}*x + {filestr}'
            else:
                filestr = f'{num}*x^{i} + {filestr}'
    filestr = f'k={k} => {filestr}\n'
    with open('task3.txt', 'w') as datafile:
        datafile.writelines(filestr)


def parse_substr(parse_str: str):  # парсим подстроку, чтоб получить степень и число
    deg = 0
    if parse_str.count('x') > 0:
        num = int(parse_str[0:parse_str.index('x') - 1])
        if parse_str.count('^') > 0:
            deg = int(parse_str[parse_str.index('^') + 1:])
        else:
            deg = 1
    else:
        num = int(parse_str)
    return num, deg


def def_sign(temp_num, i, mxrange):  # определяем знак числа
    if temp_num > 0:
        sym = '' if i == mxrange else ' + '
    else:
        sym = '-' if i == mxrange else ' - '
    return sym


def write_res(res1, res2):  # формирование результирующей строки
    temp_str = ''
    mxrange = max(max(res1.keys()), max(res2.keys()))  # берем макс из максимумов степеней многочленов для цикла
    for i in range(mxrange, 0, -1):  # тогда точно все операнды попадут
        if i in res2.keys() and i in res1.keys():  # в случае, если число i есть в обоих многочленах:
            res1_temp = res1[i] + res2[i]
            temp_str += def_sign(res1_temp, i, mxrange) + str(abs(res1_temp)) + '*x'
        else:  # а если не в обоих
            num = res1[i] if res1.get(i) else res2[i]  # то ищем в каком и берем значение
            temp_str += def_sign(num, i, mxrange) + str(abs(num)) + '*x'  # и его записываем
        if i > 1:  # а если степень  больше 0, то ее тоже надо записать
            temp_str += '^' + str(i)
    if res1.get(0) and res2.get(0):  # для того, который без х
        temp_str += ' + ' + str(res1[0] + res2[0]) if res1[0] + res2[0] > 0 else ' - ' + str(abs(res1[0] + res2[0]))
    elif res1.get(0):
        temp_str += ' + ' + str(abs(res1[0])) if res1[0] > 0 else ' - ' + str(abs(res1[0]))
    else:
        temp_str += ' + ' + str(abs(res2[0])) if res2[0] > 0 else ' - ' + str(abs(res2[0]))
    temp_str += ' = 0'
    return temp_str


def parsing_data(polynome):
    i = 0
    parsed_dict = {}
    while True:
        sign = 1
        if polynome[i] != '+' and polynome[i] != '-':
            if polynome[i][0] == '-':
                sign = 0
                polynome[i] = polynome[i][1:len(polynome[i])]
        else:
            sign = 1 if polynome[i] == '+' else 0
            i += 1
        (num, deg) = parse_substr(polynome[i])
        if not sign: num = -num
        parsed_dict[deg] = num
        i += 1
        if i >= len(polynome): break
    return parsed_dict


def task4():
    parsed_dict1, parsed_dict2 = {}, {}  # будут храниться в словарях
    with open('task4_1.txt', 'r') as datafile:  # читаем данные из файлов
        polynome1 = list(datafile.readline().strip()[:-4].split(' '))
    with open('task4_2.txt', 'r') as datafile:
        polynome2 = list(datafile.readline().strip()[:-4].split(' '))

    parsed_dict1 = parsing_data(polynome1)
    parsed_dict2 = parsing_data(polynome2)

    if len(parsed_dict1) >= len(parsed_dict2):
        final_str = write_res(parsed_dict1, parsed_dict2)
    else:
        final_str = write_res(parsed_dict2, parsed_dict1)
    with open('task4_res.txt', 'w') as datafile:
        datafile.writelines(final_str)
        print('Выполнено')


while True:
    try:
        num = int(input('Всего у нас 4 задачи. Какой номер решить? (для выхода введите q) '))
    except ValueError:
        print('Пойду я отсюда')
        break
    else:
        if num == 1:
            print('Вычислить число c заданной точностью d')

            # для  варианта со строкой. проблема - в строке должна быть точка.
            # print(f'Число: {pi}\nПолученное число: ',
            #       task1var(input('Введите точность числа: ')))

            # для варианта с числом. проблема - иногда меняются из-за "особенностей хранения float"
            # print(f'Число: {pi}\nПолученное число: ',
            # task1(float(input('Введите точность числа: ')),pi))

            # для варианта с библиотекой. нет проблем.
            print(
                Decimal(pi).quantize(
                    Decimal(input('Введите точность числа: ')),
                    ROUND_FLOOR
                )
            )
        elif num == 2:
            print('Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся '
                  'элементов исходной последовательности.')
            task2()
        elif num == 3:
            print('Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 '
                  'до 100) многочлена и записать в файл многочлен степени k(до 6 степени)')
            task3()
        elif num == 4:
            print(
                'Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.')
            task4()
