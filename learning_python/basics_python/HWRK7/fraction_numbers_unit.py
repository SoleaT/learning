# обработка выражений с рациональными дробями
# ограничения:
# есть всего 2 числа и одна операция
# при ошибке в написании выражения с делением выполняется сразу выход из программы без возврата в main


from fractions import Fraction
from re import split, search
from logging import write_log

class Fraction_numbers_unit:
    expression = ''

    def is_expression_ok(self, expression: str) -> bool:
        if {'-', '+', '*', '/'}.isdisjoint(expression):
            return False
        return True

    def _make_ratio(self, num: str):
        if '/' in num:
            return Fraction(int(num[:num.index('/')]), int(num[num.index('/') + 1:]))
        elif '.' in num:
            return Fraction(num)
        else:
            return Fraction(int(num))

    def parse_r_str(self, expression: str):
        opers = []
        if not {'-', '+', '*'}.isdisjoint(expression):
            expression = expression.replace(' ', '')
            opers = split('[-+*]', expression)  # разделение по рег.выражению
            sign = expression[search('[-+*]', expression).start()]
        else:
            if expression.count('/') > 1:
                opers = expression.split()  # разделение строки
            if len(opers) != 3:
                print('Ошибка в написании выражения')
                write_log('Ошибка(r):' + expression)
                exit()
            sign = opers.pop(1)
        oper1 = self._make_ratio(opers[0])
        oper2 = self._make_ratio(opers[1])
        return oper1, oper2, sign

    def operation(self, x: Fraction, y: Fraction, sign: str) -> str:
        res = -1
        match sign:
            case '+':
                res = str(x + y)
            case '-':
                res = str(x - y)
            case '*':
                res = str(x * y)
            case '/':
                res = str(x / y)
        return res
