import logging


# запись в лог и вывод на экран
def print_res(mark: str, input_str: str, res: str):
    if res == '':
        print('Возникла ошибка при вычислении.')
        logging.write_log(f'Ошибка:({mark}) {input_str} = !!!')
    else:
        print(input_str, '=', res)
        logging.write_log(f' Выполнено({mark}): {input_str} = {res}')


def print_main():  # общий запуск
    mark = input('Выберите режим работы ((c)omplex/(r)atio/(l)og output: ')

    match mark:
        case 'c':
            input_str = input('Выражение: ')
            # input_str = '1+2j + 2+4j'  # debug
            cmplx = Complex_unit(input_str)
            while True:
                if not cmplx.is_expression_ok(input_str):
                    print('Ну вот сразу что-то пошло не так. Попробуйте заново (q для выхода): ')
                    input_str = input('Выражение: ')
                    if input_str == 'q':
                        exit()
                else:
                    break
            print_res(mark,
                      input_str,
                      cmplx.make_operation(*cmplx.parse_c_str(input_str))
                      )

        case 'r':
            print('Допустимые форматы ввода чисел - a/b a.b')
            input_str = input('Если используете операцию деления для дробей, отделите её пробелами: ')
            frcnum = Fraction_numbers_unit(input_str)
            # input_str = '2/4+3/4' #debug
            while True:
                if not frcnum.is_expression_ok(input_str):
                    print('Невозможно прочесть, введите заново (q для выхода): ')
                    input_str = input('Выражение: ')
                    if input_str == 'q':
                        exit()
                else:
                    break
            print_res(
                mark,
                input_str,
                frcnum.operation(*frcnum.parse_r_str(input_str))
            )
        case 'l':
            logging.view_log()
        case _:
            exit()
