import threading
from processes_work import get_image
from random import sample
from pathlib import Path
from time import time

DIRECTORY = 'threads_images'


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
        t = threading.Thread(target=save_images, args=[url])
        t.start()
    else:
        threads = []
        for u in sample(url, min(10, len(url))):
            t = threading.Thread(target=save_images, args=[u])
            threads.append(t)
            t.start()
        for t in threads:
            t.join()


if __name__ == '__main__':
    pass
