import re


def read_number(input_str: str) -> int | float | bool:
    if input_str.isdigit():
        output_str = int(input_str)
    elif re.match(r'\d*\.\d*', input_str):
        output_str = float(input_str)
    else:
        output_str = False
    return output_str
