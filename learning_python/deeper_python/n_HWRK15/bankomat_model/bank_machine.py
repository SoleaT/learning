from bankomat_settings import *
from output import *


class WrongDepositError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Проблема с деньгами: {self.value}"


class BankMachine:

    def __init__(self, deposit: float):
        self.deposit = deposit
        self.__operation_count = 0

    @staticmethod
    def check_sum(cur_money: float) -> bool:
        return True if cur_money % MULTIPLE == 0 else False

    def _pickup_deposit(self, cur_money: float):
        self.deposit -= cur_money
        self.__operation_count += 1
        self._add_bonus()
        logger.info(f'Снято с процентами {cur_money} денях. Счёт: {self.deposit}')
        return f'Снято с процентами {cur_money} денях'

    def _print_deposit(self):
        self.__operation_count += 1
        self._add_bonus()
        logger.info(f'Запросили показать счёт. Счёт: {self.deposit}')
        return f'На счету {self.deposit:.2f} средств'

    def _too_rich(self):
        if self.deposit > COMMUNISM:
            self.deposit = self.deposit * (1 - DEKULAKIZATION)
            logger.info(f'Снят налог на богатство')
            print_user_data('Вы слишком богаты, мы украли чуток ваших денях')
        return

    def _add_bonus(self):
        if self.__operation_count == WONDERFUL_OPERATION:
            self.deposit += self.deposit * BONUS
            self.__operation_count = 0
            logger.info(f'К счету добавлен бонус')
            print_user_data(f'Для вас бонус - увеличили счёт на {BONUS * 100}%')

    def _restock_deposit(self, cur_money: float):
        self.deposit += cur_money
        self.__operation_count += 1
        self._add_bonus()

    def start_work(self):
        while True:
            choicekey = input_user_data('Выберите операцию: 1 - пополнить, 2 - снять, 3 - посмотреть счет, 4 - выход: ')
            self._too_rich()
            match choicekey:
                case '1':
                    money = None
                    try:
                        money = input_float_user_data('На какое кол-во хотите пополнить? ')
                    except Exception as e:
                        logger.warning(f'Ввели цифры вместо букв, ой, то есть наоборот {e}')
                        print_user_data(f'Нифига неправильно ввели сумму. Вам надо клаву только на цифры дать?')
                    if money:
                        if self.check_sum(money):
                            self._restock_deposit(money)
                        else:
                            logger.critical(f'Хотели пополнить на сумму, не кратную {MULTIPLE}')
                            raise WrongDepositError('Сумма должна быть кратна 50 уёв')

                case '2':
                    money = input_float_user_data('Сколько хотите снять? ')
                    if self.check_sum(money):
                        percent = money * PICKUP_PERCENT
                        if percent < MIN_MONEY:
                            percent = MIN_MONEY
                        elif percent > MAX_MONEY:
                            percent = MAX_MONEY
                        money += percent
                        if money > self.deposit:
                            logger.critical(
                                f'На счету недостаточно средств. Лежит {self.deposit}, хотели снять {money}')
                            raise WrongDepositError('На счету недостаточно средств')
                        else:
                            print_user_data(self._pickup_deposit(money))
                    else:
                        logger.critical(f'Хотели снять некратную сумму {money}')
                        raise WrongDepositError('Сумма должна быть кратна 50 уёв')
                case '3':
                    print_user_data(self._print_deposit())
                case _:
                    break


if __name__ == '__main__':
    client = BankMachine(0)
    client.start_work()
