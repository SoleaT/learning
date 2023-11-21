# Реализуйте алгоритм генерации случайного числа.(Не используя библиотеки связанные с рандомом)
import datetime as t
import time


def prng(bbottom=-10,btop=10):
    if bbottom<0:
        btop+=abs(bbottom)
    seed=int(t.datetime.now().microsecond/(1000000/btop))
    return seed-abs(bbottom)

for _ in range(15): #для проверки
    time.sleep(0.3)
    print(prng(-50,50))
