def fib_generate():
    x = 0
    y = 1
    while True:
        yield x
        x, y = y, x + y


n = int(input('Докуда показать? '))

fib = iter(fib_generate())

for _ in range(n):
    print(next(fib))
