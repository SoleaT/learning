# формула корреляции Пирсона
# r(x,y) = sum((xi - x среднее арифм)*(yi - y среднее арифм))/sqrt(sum(xi-x среднее арифм)^2*sum(yi - y среднее арифм))
from math import sqrt


def correlation_P(list1, list2):
    x_mean = sum(list1) / len(list1)
    y_mean = sum(list2) / len(list2)

    def r(a, a_mean):
        return a - a_mean

    return list(
        map(lambda x, y: sum(r(x, x_mean) * r(y, y_mean)) / sqrt(sum(r(x, x_mean)) ** 2 * sum(r(y, y_mean)) ** 2),
            list1, list2))


l1 = [1, 3, 2, 5, 6]
l2 = [3, 2, 5, 6, 2]
print(correlation_P(l1, l2))
