def init_task2():
    origin_list = [1, 2, 2, 5, 5, 5, 6, 7, 7, 8, 9, 10, 10]
    print(f'Исходный список: {origin_list}')
    double_items = set([item for item in origin_list if origin_list.count(item) > 1])
    print(f'Результат: {double_items}')
    return
