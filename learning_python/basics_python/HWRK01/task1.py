# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.

try:
    dayOfWeek = int(input('Введите день недели: '))
except ValueError:
    print('Неправильно задано число')
else:
    print("Рабочий день" if dayOfWeek < 6 else "Выходной день") if 0 < dayOfWeek <= 7 else print('Это не день недели')