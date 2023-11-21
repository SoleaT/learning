from sys import argv


def str_to_date(s: str) -> bool:
    try:
        day, month, year = map(int, s.split('.'))
        if 9999 < year < 1 > month > 12 and 1 > day > 31:
            return False
        return True
    except():
        return False


def check_leap_year(y: int):
    if y % 400 or y % 4:
        return True
    else:
        return False


if __name__ == '__main__':
    # s = input('Введите дату в формате DD.MM.YYYY: ')
    # s = '10.11.1700'
    s = argv[1]
    print('Дата существует' if str_to_date(s) else 'Дата не существует')
