import csv
import json
from math import sqrt
from random import randint

FILENAME = 'random_digits.csv'


def random_csv_write():
    data = []
    for _ in range(randint(100, 1000)):
        data.append(randint(1, 100) for _ in range(3))
    with open(FILENAME, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writerows(data)


def run_with_file_data(func):
    def wrapper(*args):
        with open(FILENAME, 'r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
            ext = {}
            for line in csv_reader:
                ext[str(line)] = func(*line)
        return ext

    return wrapper


def write_to_json(func):
    def wrapper(*args):
        result_dict = dict(func(*args))
        with open('solutions.json', 'w') as json_file:
            json.dump(result_dict, json_file, indent=2, ensure_ascii=False)
        return result_dict

    return wrapper


@write_to_json
@run_with_file_data
def quadratic(a, b, c):
    d = b ** 2 - 4 * a * c
    if d == 0:
        x2 = x1 = - b / (2 * a)
    elif d > 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
    else:
        x1 = (-b + d ** 0.5) / 2 * a
        x2 = (-b - d ** 0.5) / 2 * a
    return str(x1), str(x2)


quadratic(1, 2, 1)

# random_csv_write()
