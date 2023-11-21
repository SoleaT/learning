import datetime
from pprint import pprint
from random import randint

from io_module import *

DISCIPLINE_LIST = [''.join(i) for i in read_csv_data('discipline.txt')]
TESTS_COUNT = 5


class TrueName:
    # def __init__(self, pname):
    # self.pname = pname

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.check_name(value):
            setattr(instance, self.name, value)
        else:
            setattr(instance, self.name, str(value).title())

    @classmethod
    def check_name(cls, str_value: str):
        if str_value.isalpha() and str_value.istitle():
            return True
        return False


class Person:
    name = TrueName()
    surname = TrueName()
    midname = TrueName()

    def __init__(self, name, surname, midname, birth_date: datetime):
        self.name = name
        self.surname = surname
        self.midname = midname
        self.birth_date = birth_date


class Student(Person):

    def __init__(self, name, surname, midname, birth_date: datetime, acquisition_year):
        super().__init__(name, surname, midname, birth_date)
        self.acquisition_year = acquisition_year
        self.rates = self.__read_rates()
        self.tests = self.__read_tests()

    @staticmethod
    def __read_rates():
        rates = {}
        for disc in DISCIPLINE_LIST:
            # s=input(f'Введите оценки по {disc}: ')
            s = ' '.join([str(randint(2, 5)) for i in range(randint(1, 10))])
            try:
                rates[disc] = (list(map(int, s.split())))
            except Exception as e:
                raise ValueError(f'Возникла ошибка при обработке оценок {e}')
        return rates

    @staticmethod
    def __read_tests():
        tests = {}
        for disc in DISCIPLINE_LIST:
            # s=input(f'Введите результаты тестов по {disc}: ')
            s = ' '.join([str(randint(0, 100)) for i in range(TESTS_COUNT)])
            try:
                tests[disc] = (list(map(int, s.split())))
            except Exception as e:
                raise ValueError(f'Возникла ошибка при обработке результатов тестов {e}')
        return tests

    def count_test_average(self):
        temp_dict = {}
        for k, v in self.tests.items():
            temp_dict[k] = (sum(v) / len(v))
        return temp_dict

    def count_all_rates(self):
        temp = 0
        for v in self.rates.values():
            temp += sum(v) / len(v)
        return temp / len(DISCIPLINE_LIST)

    def __str__(self):
        return f'{self.name} {self.midname} {self.surname}, {self.birth_date.year} года рождения.\n' \
               f'Оценки: {self.rates}\n' \
               f'Результаты тестов: {self.tests}\n'


if __name__ == '__main__':
    student = Student('уаася', 'пупкен', 'стоеросович', datetime.date(1999, 5, 15), datetime.datetime.now().year)
    print(student)
    print(f'Средняя оценка по всем предметам: {student.count_all_rates():.2f}')
    print(f"Средняя оценка тестов по предметам:")
    pprint(student.count_test_average())
