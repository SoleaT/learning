def init_task1():
    tour = {
        'Петя': ('спички', 'сахар', 'сгущенка', 'соль', 'фонарь', 'палатка', 'спальный мешок'),
        'Вася': ('спички', 'кружка', 'сгущенка', 'соль', 'фляжка', 'презервативы', 'спальный мешок'),
        'Мотя': ('картошка', 'кружка', 'сгущенка', 'нож', 'фонарь', 'спальный мешок'),
        'Олег': ('фонарь', 'термос', 'кружка', 'чугунок', 'соль', 'сгущенка', 'спальный мешок')
    }

    print('\nДрузья собрались в поход в следующем составе и с вещами: ')
    for key, item in tour.items():
        print(f'{key} взял: ', *item)
    print('-' * 100)
    # all_items = set.intersection(*tour.values())
    # Выводим вещи, которые взяли все друзья
    items_in_common = set.intersection(*(set(items) for items in tour.values()))
    print("Вещи, которые взяли все друзья: ", *items_in_common)
    # Выводим уникальные вещи, которые есть только у одного друга
    unique_items = set.union(*[set(items) for items in tour.values()]) - items_in_common
    print("Уникальные вещи, которые есть только у одного из друзей: ", *unique_items)
    # Выводим вещи, которые есть у всех друзей, кроме одного, и имя друга, у которого отсутствует данная вещь
    for key_name, items in tour.items():
        other_friends = set.intersection(*[set(item) for key, item in tour.items() if key != key_name])
        missing_items = other_friends - set(items)
        if missing_items:
            print(f"У всех друзей, кроме {key_name}, есть следующие вещи, которых у него нет: ", *missing_items)
    print('-' * 100)
    return
