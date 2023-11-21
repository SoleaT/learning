from random import randint
from sys import argv

from deeper_python.n_HWRK06 import iomod


def hit_digit(right, left, attempts):
    random_num = randint(right, left)
    for i in range(attempts):
        attempt = iomod.read_number(input(f'Угадай число с {attempts - i} попыток: '))
        if attempt > random_num:
            print('Не угадал, число меньше.')
        elif attempt < random_num:
            print('Не угадал, число больше')
        else:
            return True
    else:
        return False


if __name__ == '__main__':
    new_list = [int(x) for x in argv[1:]]
    right_boundary = new_list[0] if new_list else iomod.read_number(input('Правая граница: '))
    left_boundary = new_list[1] if len(new_list) > 1 else iomod.read_number(input('Левая граница: '))
    attempts = new_list[2] if len(new_list) > 2 else iomod.read_number(input('К-во попыток: '))
    if hit_digit(right_boundary, left_boundary, attempts):
        print('Число угадано')
    else:
        print('Число попыток исчерпано')
