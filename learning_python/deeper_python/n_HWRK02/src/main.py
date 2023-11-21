from deeper_python.n_HWRK02.src.io import read_number
from deeper_python.n_HWRK02.src.tasks import init_task1, init_task2

NUMBER_OF_TASKS = 2


def start_work():
    with open('../tasks_text.txt', 'r', encoding='utf-8') as tasks_text_file:
        tasks_text = [line.strip() for line in tasks_text_file]
    while True:
        key = read_number(input('Какую задачу запустить? Для выхода введите любой символ, кроме номеров задач '
                                f'(задач всего {NUMBER_OF_TASKS}) '))
        if not key or key > NUMBER_OF_TASKS:
            print('Выход')
            break
        print(tasks_text[key - 1])
        match key:
            case 1:
                decimal_number = read_number(input('Задайте число для перевода в шестнадцатеричное представление: '))
                init_task1(decimal_number)
            case 2:
                init_task2()
            case _:
                print('Такой задачи нет')
                break


start_work()
