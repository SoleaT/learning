import csv
import os
import json
import pickle
from pprint import pprint

req_dir = os.getcwd()


def hwrk8():
    def dir_size(current_dir):  # считает размер директорий с поддиректориями
        a = os.listdir(current_dir)
        size = 0
        for item in a:
            item = current_dir + '\\' + item
            if os.path.isfile(item):
                size = os.path.getsize(item) + size
            if os.path.isdir(item):
                size = dir_size(item) + size
        return size

    with (open('thisdir.json', "w", encoding='utf-8') as json_file,
          open('thisdir.csv', 'w', encoding='utf-8', newline='') as csv_file,
          open('thisdir.pickle', 'wb') as pickle_file):

        new_dict = {}

        for dir_path, dir_name, file_name in os.walk(req_dir):
            new_dict[dir_path] = {'directory size': dir_size(dir_path), 'subdirectories': dir_name, 'files': {}}

            files_list = {}
            for f in file_name:
                files_list[f] = os.path.getsize(dir_path + '\\' + f)
            new_dict[dir_path].get('files').update(files_list)

        # pprint(new_dict)

        # запись в json
        json.dump(new_dict, json_file, indent=2, ensure_ascii=False)

        # запись в csv
        fieldnames = ['directory name', 'directory size', 'subdirectories', 'files']
        csv_txt = csv.DictWriter(csv_file, fieldnames=fieldnames, quoting=csv.QUOTE_NONNUMERIC, delimiter=';')
        csv_txt.writeheader()
        for key, line in new_dict.items():
            line.update({'directory name': key})
            csv_txt.writerow(line)

        # запись в pickle
        pickle.dump(new_dict, pickle_file, protocol=pickle.DEFAULT_PROTOCOL, )


if __name__ == '__main__':
    hwrk8()
