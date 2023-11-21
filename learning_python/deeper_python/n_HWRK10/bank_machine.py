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
        return True if cur_money % 50 == 0 else False

    def _pickup_deposit(self, cur_money: float):
        self.deposit -= cur_money
        self.__operation_count += 1
        self._add_bonus()
        return f'Снято с процентами {cur_money} денях'

    def _print_deposit(self):
        return f'На счету {self.deposit:.2f} средств'

    def _too_rich(self):
        if self.deposit > 5_000_000:
            self.deposit = self.deposit * 0.9
            print_user_data('Вы слишком богаты, мы украли чуток ваших денях')
        return

    def _add_bonus(self):
        if self.__operation_count == 3:
            self.deposit += self.deposit * 0.03
            self.__operation_count = 0
            print_user_data('Для вас бонус - увеличили счёт на 3%')

    def _restock_deposit(self, cur_money: float):
        self.deposit += cur_money
        self.__operation_count += 1
        self._add_bonus()

    def start_work(self):
        while True:
            choicekey = input('Выберите операцию: 1 - пополнить, 2 - снять, 3 - посмотреть счет, 4 - выход: ')
            self._too_rich()
            match choicekey:
                case '1':
                    money = float(input('На какое кол-во хотите пополнить? '))
                    if self.check_sum(money):
                        self._restock_deposit(money)
                    else:
                        raise WrongDepositError('Сумма должна быть кратна 50 уёв')
                case '2':
                    money = (float(input('Сколько хотите снять? ')))
                    if self.check_sum(money):
                        percent = money * 0.015
                        if percent < 30:
                            percent = 30
                        elif percent > 600:
                            percent = 600
                        money += percent
                        if money > self.deposit:
                            raise WrongDepositError('На счету недостаточно средств')
                        else:
                            print(self._pickup_deposit(money))
                    else:
                        raise WrongDepositError('Сумма должна быть кратна 50 уёв')
                case '3':
                    print_user_data(self._print_deposit())
                case _:
                    break


def print_user_data(s: str):  # чтобы модно
    print(f'Банкомат сказал: {s}')


client = BankMachine(0)
client.start_work()
