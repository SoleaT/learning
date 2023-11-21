def parse_str(tempstr: str):
    ready = [int(i) if i.isdigit() else i for i in tempstr.replace(' ', '')]
    if ready[0] == '-':
        ready.pop(0)
        ready[1] = -ready[1]
    return ready


def oper(x, op, y):
    match op:
        case '+':
            return x + y
        case '-':
            return x - y
        case '*':
            return x * y
        case '/':
            return x // y


def rem_parenthesis(expr_parsed):
    left_index, i = 0, 0
    while not {'(', ')'}.isdisjoint(expr_parsed):
        left_index = i if expr_parsed[i] == '(' else left_index
        if expr_parsed[i] == ')':
            temp_arr = expr_parsed[left_index + 1:i]
            expr_parsed = [*expr_parsed[:left_index], oper(*temp_arr), *expr_parsed[i + 1:]]
            i = 0
        else:
            i += 1
    return expr_parsed


def evaluate(expr_parsed):
    expr_parsed = rem_parenthesis(expr_parsed)

    while len(expr_parsed) > 1:
        if '*' in expr_parsed or '/' in expr_parsed:
            if not '*' in expr_parsed:
                idx = expr_parsed.index('/')
            elif not '/' in expr_parsed:
                idx = expr_parsed.index('*')
            else:
                idx = expr_parsed.index('*') if expr_parsed.index('*') < expr_parsed.index('/') else expr_parsed.index(
                    '/')
            expr_parsed = [*expr_parsed[:idx - 1], oper(*expr_parsed[idx - 1:idx + 2]), *expr_parsed[idx + 2:]]
        elif '+' in expr_parsed or '-' in expr_parsed:
            if not '-' in expr_parsed:
                idx = expr_parsed.index('+')
            elif not '+' in expr_parsed:
                idx = expr_parsed.index('-')
            else:
                idx = expr_parsed.index('+') if expr_parsed.index('+') < expr_parsed.index('-') else expr_parsed.index(
                    '-')
            expr_parsed = [*expr_parsed[:idx - 1], oper(*expr_parsed[idx - 1:idx + 2]), *expr_parsed[idx + 2:]]
    return expr_parsed
