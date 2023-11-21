# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка
while True:
    try:
        x, y = int(input('Введите x: ')), int(input('Введите y: '))
        break
    except ValueError:
        print('Что-то пошло не так. Введите данные заново')

if x == 0 or y == 0:
    print('Координаты на оси')
elif x > 0:
    if y > 0:
        print('I четверть')
    else:
        print('IV четверть')
else:
    if y > 0:
        print('II четверть')
    else:
        print('III четверть')
