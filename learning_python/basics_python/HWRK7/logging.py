# модуль записи и чтения лога

import datetime


def write_log(str):
    timenow = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    with open('calc_log.txt', 'a') as calc_log:
        calc_log.writelines(timenow + str + '\n')


def view_log():
    with open('calc_log.txt', 'r') as calc_log:
        for i in calc_log:
            print(i.rstrip())

