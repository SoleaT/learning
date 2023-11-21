import asyncio
import aiofiles
from aiohttp import ClientSession
from pathlib import Path
from random import sample
from time import time

DIRECTORY = 'async_images'


async def get_image(session, url):
    try:
        response = await session.request(method="GET", url=url)
        return response
    except Exception as e:
        print(e)
        return False


# для записи используем библиотеку aiofiles, пусть она всего лишь на потоках, но это всё равно мультизадачность
async def save_images(url):
    sufxes = ('jpg', 'jpeg', 'gif', 'svg', 'png')
    async with ClientSession() as session:
        response = await get_image(session, url)
        if response and response.status == 200:
            if url.endswith(sufxes):
                start_time = time()
                image_path = f"{DIRECTORY}/{url.split('/')[-1]}"
                if not Path(DIRECTORY).exists():
                    Path(DIRECTORY).mkdir()
                async with aiofiles.open(image_path, 'wb') as file:
                    await file.write(await response.read())
                print(f'Время скачивания файла: {time.time() - start_time:.2f} sec')
        else:
            raise Exception('Невозможно прочитать файл')


async def main(url):
    if isinstance(url, str):
        task = asyncio.create_task(save_images(url))
        await task
    else:
        tasks = []
        for u in sample(url, min(10, len(url))):
            task = asyncio.create_task(save_images(u))
            tasks.append(task)
        await asyncio.gather(*tasks)

# asyncio.run(main(read_file_links('links.txt')))
