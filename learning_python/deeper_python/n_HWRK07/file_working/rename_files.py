from pathlib import Path


def group_rename(dir_name, region: list, b_extension: str, e_extension: str, num_of_digits=2, filename=''):
    a = Path(dir_name)
    count = 1
    for i in a.iterdir():
        if i.suffix != '.' + b_extension:
            continue
        new_filename = str.format(i.name[region[0]:region[1]] +
                                  filename +
                                  str(count).rjust(num_of_digits, '0') +
                                  '.' +
                                  e_extension)
        count += 1
        Path(i).rename(dir_name + '/' + new_filename)
        print(f'Файл{i} переименован в{new_filename}')


if __name__ == '__main__':
    group_rename('temp', [3, 6], 'txt', 'xxt', 3, 'renamed', )
