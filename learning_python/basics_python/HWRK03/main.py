import functions

while True:
    try:
        num = int(input('Всего у нас 4 задачи. Какой номер решить? (для выхода введите q) ')) #вообще по любому символу работает :(
    except ValueError:
        print('Пойду я отсюда')
        break
    else:
        if num == 1:
            functions.task1(int(input('Какого размера список сгенерировать? ')))
        elif num == 2:
            functions.task2()
        elif num == 3:
            functions.task3(int(input('Какое число перевести в двоичное? ')))
        elif num == 4:
            lst_fib = [1, 0, 1]                                                              #начальное значение списка
            print(functions.task4(lst_fib, int(input('Сколько чисел Нефигабоначчи вывести? '))))

