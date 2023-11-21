# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# часть 1: шифровка
with open('task4_org.txt', 'r') as datafile:
    original_txt = ''.join(line.strip() for line in datafile)

temp_str, result_str = original_txt[0], ''
i = 0

for dchar in original_txt:
    if dchar != temp_str[-1]:
        result_str += str(i) + temp_str[-1]
        i = 1
        temp_str = dchar
    else:
        i += 1
        temp_str += dchar
result_str += str(i) + temp_str[-1]

with open('task4_code.txt', 'w') as datafile:
    datafile.writelines(result_str)
print(original_txt)
print(result_str)

# часть 2: расшифровка
with open('task4_code.txt', 'r') as datafile:
    code_txt = ''.join(line.strip() for line in datafile)

result_str = ''
for dchar in code_txt:
    if dchar.isalpha():
        pchar = code_txt.index(dchar)
        num = int(code_txt[0:pchar])
        result_str += dchar * num
        code_txt = code_txt[pchar + 1:]

with open('task4_decode.txt', 'w') as datafile:
    datafile.writelines(result_str)

print('Выполнено')
print(result_str)
