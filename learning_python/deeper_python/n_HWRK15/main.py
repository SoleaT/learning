from bankomat_model.bank_machine import BankMachine
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Количество денег для банкомата')
    parser.add_argument('deposit', metavar='D', type=float, nargs=1, help='Начальный депозит в банкомате, число')
    args = parser.parse_args()

    client = BankMachine(args.deposit[0])
    client.start_work()
