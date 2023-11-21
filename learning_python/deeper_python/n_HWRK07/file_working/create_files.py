from random import sample, randint, randbytes
from string import ascii_letters
from pathlib import Path

extensions = ['txt', 'mp3', 'doc', 'non', 'jpg']


def create_random_files(dir_name):
    if not Path(dir_name).exists():
        Path(dir_name).mkdir()
    names = set()
    while len(names) < 10:
        names.add(''.join(sample(ascii_letters, 20)))
    for name in names:
        with open(f'{dir_name}/{name}.{extensions[randint(0, len(extensions) - 1)]}', 'wb') as file:
            temp = randbytes(randint(1000, 10000))
            file.write(temp)


if __name__ == '__main__':
    create_random_files('../temp')
