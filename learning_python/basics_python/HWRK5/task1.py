# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

with open('task1_1.txt', 'r') as datafile:
    txt = ''.join(line.strip() for line in datafile)

flag_rkn = 'абв'

new_txt = ' '.join(itm for itm in txt.split(' ') if itm.find(flag_rkn) == -1)
# print(new_txt)

with open('task1_2.txt', 'w') as datafile:
    datafile.writelines(new_txt)
