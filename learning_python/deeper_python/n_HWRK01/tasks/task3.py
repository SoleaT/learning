# ✔Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать
# «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код: from random import randint num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

from deeper_python.n_HWRK01.io import read_number


def computer_generate() -> int:
    return randint(0, 1000)


def human_generate() -> int:
    num = read_number(input('Загадайте число: '))
    while not num:
        num = read_number(input('Это не число. Загадайте число: '))
    return num


def init_task3():
    who = read_number(input('Кто будет загадывать число? Человек - 0, комп - эникей: '))
    match who:
        case 0:
            generated_num = human_generate()
        case _:
            generated_num = computer_generate()
    lower_limit, upper_limit = 0, 1000
    print(f'Загадано число {generated_num}')
    for i in range(1, 11):
        guess_number = (upper_limit - lower_limit) // 2 + lower_limit
        print(f'Попытка № {i}. Предполагаю число {guess_number}')
        if guess_number > generated_num:
            print('Меньше')
            upper_limit = guess_number
        elif guess_number < generated_num:
            print('Больше')
            lower_limit = guess_number
        else:
            print('Угадал')
            break
    return
