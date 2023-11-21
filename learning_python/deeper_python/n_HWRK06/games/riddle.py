from random import choice

from deeper_python.n_HWRK06.iomod import read_number

__all__ = ['one_random_riddle', 'loop_riddles', 'print_stat']
riddles = {
    'Какого черта? ': ['лысого', 'пьяного', 'красного'],
    '''Он морж, она - моржиха.
    Он заяц, она - зайчиха.
    Он бык, она - ''': ['бычиха'],
    'Не лёд, а тает, не лодка, а уплывает. ': ['зарплата'],
    'Какого цвета огонь? ': ['зеленого', 'оранжевого', 'голубого']
}

_answers_stat = {}


def get_riddle(r_text: str, r_var, x: int = 1) -> int:
    for i in range(x):
        s = input('Ваш вариант? ')
        if s.lower().strip() in r_var:
            _answers_stat[r_text] = i + 1
            return i + 1
        else:
            print('Неверно.')
    else:
        return 0


def loop_riddles():
    for k, v in riddles.items():
        print(f'Загадка: \n {k}')
        result = get_riddle(k, v, read_number(input('Сколько попыток дать? ')))
        if result:
            print(f'Правильно, угадано с {result} попытки.')
        else:
            print('Попытки закончились, загадка не угадана')


def one_random_riddle():
    riddle = choice(list(riddles.keys()))
    print(f'Выбрана загадка: \n {riddle}')
    result = get_riddle(riddle, riddles[riddle], read_number(input('Сколько попыток дать? ')))
    if result:
        print(f'Правильно, угадано с {result} попытки.')
    else:
        print('Попытки закончились, загадка не угадана')


def print_stat():
    print(*(f'\nЗагадка "{k}" угадана с {v} попытки.' for k, v in _answers_stat.items()))


if __name__ == '__main__':
    loop_riddles()
    print_stat()
