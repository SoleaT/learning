class Calculator:
    @staticmethod
    def calculation(first_operand: int, second_operand: int, operator: chr):
        match operator:
            case '+':
                return first_operand + second_operand
            case '-':
                return first_operand - second_operand
            case '*':
                return first_operand * second_operand
            case '/':
                if second_operand != 0:
                    return first_operand / second_operand
                else:
                    raise ZeroDivisionError('Division by zero is not possible')
            case _:
                raise ValueError('Unexpected value operator: ' + operator)

    @staticmethod
    def square_root_extraction(number: float):
        if number < 0:
            raise ValueError('It is impossible to extract the root from negative numbers')
        elif not number:
            raise ValueError('It is not possible to extract the root from 0')
        return number ** 0.5

    @staticmethod
    def calculating_discount(purchase_amount: float, discount_amount: int):
        if discount_amount > 100:
            raise ValueError("Amount can't be greater than 100%")

        return purchase_amount - purchase_amount * discount_amount / 100
