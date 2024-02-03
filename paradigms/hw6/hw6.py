import random


def binary_search(x, arr):
    left_index = 0
    right_index = len(arr) - 1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        if x == arr[mid_index]:
            return mid_index
        elif x < arr[mid_index]:
            right_index = mid_index -1
        else:
            left_index = mid_index + 1
    return -1


if __name__ == '__main__':
    c = random.randint(30, 70)
    a = [i + 1 for i in range(random.randint(30, 100))]
    print(f'Число {c} ищем в массиве {a}')

    if binary_search(c, a) == -1:
        print('Не найдено')
    else:
        print(binary_search(c, a))
