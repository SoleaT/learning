def input_user_data(s: str):
    return input(s)


def input_float_user_data(s: str):
    a = input(s)
    try:
        b = float(a)
    except Exception as e:
        raise
    else:
        return b
