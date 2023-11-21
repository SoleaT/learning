# Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для
# проверки: «Число является простым, если делится нацело только на единицу и на себя». Сделайте ограничение на ввод
# отрицательных чисел и чисел больше 100 тысяч.

from deeper_python.n_HWRK01.io import read_number


# оптимизированный перебор делителей. страшно в решето Эратосфена соваться


def init_task2() -> str:
    key_num = read_number(input('Введите число: '))
    if not key_num:
        return 'Это не число'
    if key_num < 0 or key_num > 100000:
        return 'Число не подходит'
    flag = False
    i = 2
    while i * i <= key_num and key_num % i != 0:
        i += 1
    if i * i > key_num:
        flag = True

    return 'Число составное' if flag is False else 'Число простое'
