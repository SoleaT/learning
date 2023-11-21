import fractions
import math

from deeper_python.n_HWRK02.src.io import read_number


def init_task1(decimal_number: int):
    print(f'При использовании функции hex: {hex(decimal_number)}')
    hex_str = ''
    hex_digits = '0123456789abcdef'
    if decimal_number == 0:
        print('Число в hex = 0')
        return
    while decimal_number > 0:
        temp = decimal_number % 16
        hex_str = hex_digits[temp] + hex_str
        decimal_number = decimal_number // 16
    print(f'При использовании самодельной функции: 0х{hex_str}')

    return


def sum_fraction(fraction):
    if fraction[1] != fraction[3]:
        temp = fraction[1]
        fraction[0] *= fraction[3]
        fraction[1] *= fraction[3]
        fraction[2] *= temp
    new_numerator = fraction[0] + fraction[2]
    common_divisor = math.gcd(new_numerator, fraction[1])
    new_numerator //= common_divisor
    fraction[1] //= common_divisor
    return new_numerator, fraction[1]


def mult_fraction(fraction):
    new_numerator = fraction[0] * fraction[2]
    new_nominator = fraction[1] * fraction[3]
    new_common_divisor = math.gcd(new_numerator, new_nominator)
    return new_numerator // new_common_divisor, new_nominator // new_common_divisor


def init_task2():
    fractions_list = input('Дроби в формате x1/y1 x2/y2: ').replace('/', ' ').split(' ', 4)
    fractions_list.pop() if len(fractions_list) > 4 else fractions_list
    fractions_list = list(map(read_number, fractions_list))

    if not fractions_list or len(fractions_list) < 4 or False in fractions_list:
        print('Неправильный ввод дроби')
        return

    print('Результат сложения, используя модуль Fractions: ', end='')
    print(fractions.Fraction(fractions_list[0], fractions_list[1]) + fractions.Fraction(fractions_list[2],
                                                                                        fractions_list[3]))
    print('Результат умножения, используя модуль Fractions: ', end='')
    print(fractions.Fraction(fractions_list[0], fractions_list[1]) * fractions.Fraction(fractions_list[2],
                                                                                        fractions_list[3]))
    fractions_list_copy = fractions_list.copy()
    a, b = sum_fraction(fractions_list)
    print(f'Результат сложения, используя самодельную функцию: {a}/{b}')
    a, b = mult_fraction(fractions_list_copy)
    print(f'Результат умножения, используя самодельную функцию: {a}/{b}')
    return
