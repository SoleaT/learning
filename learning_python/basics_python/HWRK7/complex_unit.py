# обработка выражений с комплексными числами
# ограничения:
# есть всего 2 числа и одна операция

from re import search


class Complex_unit:
    expression = ''

    def __init__(self, expression: str):
        self.expression = expression

    # ну такая слабенькая проверка выражения
    def is_expression_ok(self, expression: str) -> bool:
        if expression.count('j') != 2:
            return False
        if {'-', '+', '*', '/'}.isdisjoint(expression):
            return False
        try:
            for i in range(expression.count('j')):
                if expression[expression.index('j') - 2] not in {'-', '+'}:
                    return False
        except:
            return False
        return True

    # создать комплексное число из строки. предполагается, что строка имеет вид +\-a+\-bj типа '-2+53j'
    def _make_complex(self, num: str) -> complex:
        neg1 = False  # отрицательная ли вещественная часть
        if num[0] == '-':
            neg1 = True
            num = num[1:]
        j = num.index('j') + 1  # индекс буквы в мнимой части
        sign_idx = search('[-+]', num).start()  # поиск знака
        first_num = float(num[:sign_idx]) if not neg1 else -float(num[:sign_idx])  # число вещ. части со знаком
        sec_num = float(num[sign_idx + 1:j - 1]) if num[sign_idx] == '+' else -float(
            num[sign_idx + 1:j - 1])  # и мнимой
        oper = complex(first_num, sec_num)  # преобразование в комплексное число
        return oper

    def parse_c_str(self, expression: str):
        expression = expression.replace(' ', '')
        firstj = expression.index('j')
        oper1 = self._make_complex(expression[:firstj + 1])
        sign = expression[firstj + 1:firstj + 2]
        oper2 = self._make_complex(expression[firstj + 2:])
        return oper1, oper2, sign

    def make_operation(self, x: complex, y: complex, sign: str) -> str:
        res = ''
        match sign:
            case '+':
                res = str(x + y)
            case '-':
                res = str(x - y)
            case '*':
                res = str(x * y)
            case '/':
                res = str(x / y)
        return res.replace('(', '').replace(')', '')

# print(make_operation(*parse_c_str('-2+3j - 6+3j')))  # debug
