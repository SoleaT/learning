"""Сравнение средних арифметических"""
import pytest
from average import AverageGenerator, AverageComparator


def test_find_average_type_error():
    """Тестирование на тип данных"""
    with pytest.raises(TypeError):
        AverageGenerator('Не список')


def test_find_average_empty_error():
    """Тестирование на пустоту"""
    with pytest.raises(ValueError):
        AverageGenerator()


def test_find_average_size_error():
    """Тестирование на неправильный размер"""
    with pytest.raises(ValueError):
        AverageGenerator(1, 10, 50)


def test_find_average_checker_integration():
    """Тестирование на правильный результат создание экземпляра"""
    avg1 = AverageGenerator(5, 1, 100)
    assert isinstance(avg1, AverageGenerator)


def test_find_average_end_to_end():
    """end-to-end тест"""
    avg1 = AverageGenerator(7, 5, 50)
    avg2 = AverageGenerator(7, 5, 50)
    assert AverageComparator.avg_compare(avg1.average, avg2.average)


@pytest.mark.parametrize("first_avg, second_avg, expected",
                         [(10, 5, 'Первое среднее больше, чем второе'),
                          (5, 10, 'Первое среднее меньше, чем второе'),
                          (10, 10, 'Средние арифметические равны')])
def test_is_prime(first_avg, second_avg, expected):
    """Параметризованный тест для тестирования вывода"""
    assert AverageComparator.avg_compare(first_avg, second_avg) == expected
