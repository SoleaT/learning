def to_dec(bin_str):
    temp = bin_str[::-1]
    temp = sum(int(temp[i]) * 2 ** i for i in range(len(temp)))
    return temp - 1


alpb_string = 'абвгдеёжзийклмнопрстуфxцчшщъыьэюя'

with open('ciphertext.txt', 'r') as cipher_file:
    cipher_data = [line.strip() for line in cipher_file]  # шифровка от шпиёна лежит в файле

decipher_data = {}  # расшифрованный словарь, где ключ - номер клетки, значение - зверь

for j in range(len(cipher_data)):  # тут короче какая-то магия, в результате которой получаем внятные данные
    temp = list(to_dec(cipher_data[j][i * 6:(i + 1) * 6]) for i in range(len(cipher_data[j]) // 6))
    decipher_data.update({j: ''.join(alpb_string[i + 1] for i in temp)})

print('Состав зоопарка: ')
for key in decipher_data:
    print(f"клетка {key} - {decipher_data[key]}", end='. ')  # просто вывод данных

search_animal = input('\nКакое животное найти? ')  # теперь ищем животное
try:
    print(next(f'Животное {search_animal} в клетке {key}' for key, v in decipher_data.items() if v == search_animal))
except StopIteration:
    print('Нет таких')
