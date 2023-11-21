from deeper_python.n_HWRK01.io import read_number
from deeper_python.n_HWRK01.tasks import init_task1
from deeper_python.n_HWRK01.tasks.task2 import init_task2
from deeper_python.n_HWRK01.tasks import init_task3


def start_work():
    tasks_text = []
    with open('tasks_text.txt', 'r', encoding='utf-8') as tasks_text_file:
        tasks_text = [line.strip() for line in tasks_text_file]
    while True:
        key = read_number(input('Какую задачу запустить? '))
        if not key:
            break
        print(tasks_text[key - 1])
        match key:
            case 1:
                print(init_task1())
                continue
            case 2:
                print(init_task2())
                continue
            case 3:
                init_task3()
                continue
            case _:
                print('Такой задачи нет')
                continue
