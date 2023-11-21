import csv
import os.path


def read_csv_data(filename: str) -> list | bool:
    if os.path.exists(filename):
        with open(filename, 'r', newline='', encoding='utf-8') as f:
            csv_file = csv.reader(f)
            csv_list = [line for line in csv_file]
        return csv_list
    else:
        return False


def read_csv_data_dict(filename, fields: list, rest_keys: str = 'other', rest_values: str = 'other') -> list | bool:
    if os.path.exists(filename):
        with open(filename, 'r', newline='', encoding='utf-8') as f:
            csv_file = csv.DictReader(f, fieldnames=fields, restkey=rest_keys, restval=rest_values)
            csv_dict = [line for line in csv_file]
        return csv_dict
    else:
        return False
