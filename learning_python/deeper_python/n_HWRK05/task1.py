import os


def create_paths(p):
    *_, filepath, filename = (os.path.split(os.path.abspath(p)))
    return tuple([filepath, *filename.split('.')])


print(create_paths('task1.py'))
