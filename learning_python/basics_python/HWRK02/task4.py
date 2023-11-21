# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных
# позициях. Позиции хранятся в файле file.txt в одной строке одно число.

path = 'file.txt'

num = int(input('Введите число: '))
nums = list(range(-num, num + 1))
print('Полученный список:', nums)

with open(path, 'r') as openedfile:
    data = [int(line.strip()) for line in openedfile]

if max(data) > len(nums):
    print('Максимальный индекс из файла больше, чем к-во значений в списке')
    exit()

mult = 1
for idx in data:
    mult *= nums[idx]

print(f'Произведение чисел на позициях {data} = {mult}')
openedfile.close()
