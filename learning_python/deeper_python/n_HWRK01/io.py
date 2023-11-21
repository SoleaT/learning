def read_number(input_str: str) -> int | bool:
    return int(input_str) if input_str.isdigit() else False
