# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c — стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами
# не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
from deeper_python.n_HWRK01.io import read_number


def init_task1() -> str:
    print('Введите длины сторон треугольника: ')
    a = read_number(input('Сторона а: '))
    b = read_number(input('Сторона b: '))
    c = read_number(input('Сторона c: '))
    result_string = 'Результата не получено'
    if not a or not b or not c:
        return result_string
    if a > b + c or b > a + c or c > a + b:
        result_string = 'Такого треугольника не существует'
        return result_string
    if a == b == c:
        result_string = 'Треугольник равносторонний.'
    if a == c or a == b or b == c:
        result_string = 'Треугольник равнобедренный.'
    if a != c and a != b and b != c:
        result_string = 'Треугольник разносторонний.'
    return result_string
