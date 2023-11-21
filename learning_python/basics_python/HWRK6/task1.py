import functools
import random

# Напишите программу, удаляющую из текста все слова, содержащие "абв".\
txt = 'пам абвпарам параавбм памаб памабв бууабвуууу буууууууууууу'
flag_rkn = 'абв'
print(f'Исходный текст: {txt}')
new_txt = list(filter(lambda x: flag_rkn not in x, txt.split()))
print(f'Текст с удаленными словами: {new_txt}')

# произведение чисел списка
lst = [random.randint(1, 5) for _ in range(random.randint(5, 10))]
print(*lst)
print('Произведение чисел списка:', functools.reduce(lambda x, y: x * y, lst))

# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
num_lst = random.randint(3, 15)
nums = list(range(-num_lst, num_lst + 1))
lst2 = [2, 4, 6, 8]
mult = 1
for i, num in enumerate(lst):
    if i in lst2:
        mult *= num
print(mult)


# принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.
def div(num):
    if (num % 5 == 0 and num % 10 == 0 or num % 15 == 0) and num % 30 != 0:
        return num
    else:
        return None


lst = [random.randrange(5, 300, 15) for _ in range(random.randint(5, 10))]
print('Сгенерированный список:', *lst)
print('Список чисел, кратных 5 и 10 или 15, но не 30:', list(filter(div, lst)))
