import pytest
from even_odd import even_odd_number
from interval import number_in_interval


@pytest.mark.parametrize(
    ('num', 'res'), [(3, False), (10, True), (0, True)]
)
def test_evenodd(num, res):
    assert even_odd_number(num) == res


@pytest.mark.parametrize(('num', 'res'), [(1, False), (25, True), (100, True), (45, True), (101, False)])
def test_interval(num, res):
    assert number_in_interval(num) == res


if __name__ == '__main__':
    pytest.main(['-v'])
