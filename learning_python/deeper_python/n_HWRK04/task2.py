# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.

def generate_dict(**kwargs):
    new_dict2 = {}
    for k, v in kwargs.items():
        temp = ''
        try:
            if hash(v):
                temp = v
        except:
            temp = str(v)
        new_dict2[temp] = k
    print('Переданы аргументы: ', kwargs)
    print('Полученный словарь: ', new_dict2)
    pass


generate_dict(a=frozenset([3, 'f', 'r']), b=[2, 4, 5], c=3, d={5, 7, 2})
