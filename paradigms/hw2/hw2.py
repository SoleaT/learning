# если надо обосновывать очевидные вещи,
#  структурное программирование там ну просто, чтобы красиво расположить
# а императивно выводим, потому что а как ещё
# да как будто это кто-то будет читать ))


if __name__ == '__main__':
    n=int(input('Введите н:'))
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(f'{j} x {i} = {i * j}', end='\t ')
        print('\n')
