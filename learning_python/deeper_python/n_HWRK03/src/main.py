from deeper_python.n_HWRK03.src.io import read_number
from deeper_python.n_HWRK03.src.task1 import init_task1
from deeper_python.n_HWRK03.src.task2 import init_task2
from deeper_python.n_HWRK03.src.task3 import init_task3
from deeper_python.n_HWRK03.src.task4 import init_task4

NUMBER_OF_TASKS = 4


def main():
    with open('../tasks.txt', 'r', encoding='utf-8') as tasks_text_file:
        tasks_text = [line.strip() for line in tasks_text_file]
    while True:
        key = read_number(input('Какую задачу запустить? Для выхода введите любой символ, кроме номеров задач '
                                f'(задач всего {NUMBER_OF_TASKS}) '))
        if not isinstance(key, int) or not key or key > NUMBER_OF_TASKS:
            print('Выход')
            break
        print(tasks_text[key - 1])
        match key:
            case 1:
                init_task1()
            case 2:
                init_task2()
            case 3:
                init_task3()
            case 4:
                init_task4()
            case _:
                print('Такой задачи нет')
                break


if __name__ == "__main__":
    main()
