# Напишите программу вычисления арифметического выражения заданного строкой.

import task2_functions as ff

# ваще пофик есть ли там пробелы, короче

# expr_string=input('Введите выражение: ')
# expr_string='(4 + 3) * 6 / (2 - 5) * 6'
# expr_string='1-2*3'
expr_string = '1+2*3-4/2-(5+3)*3*6/3'

expr_parsed = ff.parse_str(expr_string)
print(f'Результат {expr_string} =', *ff.evaluate(expr_parsed))
print(eval(expr_string))
