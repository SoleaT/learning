import importlib
from pathlib import Path
from sys import argv
from time import time
import processes_work
import async_work
import threads_work
from asyncio import run


def read_file_links(url):
    with open(url, 'r', encoding='utf-8') as file:
        txt = [line.strip() for line in file]
        return txt


if __name__ == '__main__':
    if len(argv) > 1:
        if Path(argv[1]).exists():
            url = argv[1]
    else:
        url = read_file_links('links.txt')
    print('''Какой метод использовать? 
          1. Потоки
          2. Процессы
          3. Асинхронность''')
    k = int(input())
    start_time = time()
    match k:
        case 1:
            threads_work.main(url)
        case 2:
            processes_work.main(url)
        case 3:
            run(async_work.main(read_file_links(url)))
        case _:
            print('Странный выбор')
    print(f'Время выполнения: {time() - start_time:.2f} sec')
