import time
import asyncio
from aiohttp import ClientSession
import aiofiles


# закачать ссылки - работа для асинк
# теория https://habr.com/ru/articles/667630/

async def get_link():
    async with ClientSession() as session:
        async with session.get('https://random.dog/woof.json') as response:  # спс за ссылку
            link_json = await response.json()
            try:
                return link_json['url'] + '\n'
            except KeyError:
                return 'Нет данных'


async def main():
    tasks = []
    for _ in range(100):
        task = asyncio.create_task(get_link())
        tasks.append(task)

    links = await asyncio.gather(*tasks)

    async with aiofiles.open('links.txt', 'w', encoding='utf-8') as file:
        await file.writelines(links)


if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    print(f'Время выполнения: {time.time() - start_time:.2f} sec')
