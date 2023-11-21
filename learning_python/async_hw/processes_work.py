import multiprocessing
import requests
from pathlib import Path
from random import sample
from time import time
DIRECTORY = 'multi_images'


def read_file_links(url):
    with open(url, 'r', encoding='utf-8') as file:
        txt = [line.strip() for line in file]
        return txt


def get_image(url):
    try:
        response = requests.get(url)
        return response
    except Exception as e:
        print(e)
        return False


def save_images(url):
    sufxes = ('jpg', 'jpeg', 'gif', 'svg', 'png')
    response = get_image(url)
    if response:
        if url.endswith(sufxes):
            start_time = time()
            image_path = f"{DIRECTORY}/{url.split('/')[-1]}"
            if not Path(DIRECTORY).exists():
                Path(DIRECTORY).mkdir()
            with open(image_path, 'wb') as file:
                file.write(response.content)
            print(f'Время скачивания файла: {time.time() - start_time:.2f} sec')
    else:
        raise Exception('Невозможно прочитать файл')


def main(url):
    if isinstance(url, str):
        p = multiprocessing.Process(target=save_images, args=(url,))
        p.start()
    else:
        procecces = []
        for u in sample(url, min(10, len(url))):
            p = multiprocessing.Process(target=save_images, args=(u,))
            procecces.append(p)
            p.start()

        for p in procecces:
            p.join()


if __name__ == '__main__':
    main(read_file_links('links.txt'))
