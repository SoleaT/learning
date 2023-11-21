from fastapi import FastAPI
from pydantic import BaseModel
from aiologger import Logger

logger = Logger.with_default_handlers(name='mylog')

app = FastAPI()


class Task(BaseModel):
    name: str
    description: str
    done: bool


tasks = {}


@app.get("/")
async def root():
    await logger.info('Отработан GET с подсказками "/" ')
    return {"availables":
                {'GET': {'return all': '/tasks', 'return one': '/tasks/{id}'},
                 'POST': {'create new': '/tasks'},
                 'PUT': {'update someone': '/tasks/{id}'},
                 'DELETE': {'delete one': '/tasks/{id}'}
                 }
            }


@app.get("/tasks")
async def get_all():
    await logger.info('Отработал GET всех задач')
    result = {}
    for i in tasks:
        result[i] = {'name': tasks[i].name, 'done': tasks[i].done, 'description': tasks[i].description}
    if result:
        return result
    return 'no tasks'


@app.get('/tasks/{id}')
async def get_task(id: int):
    await logger.info(f"Отработал GET для задачи {id}")
    if int(id) in tasks:
        return {'name': tasks[int(id)].name, 'done': tasks[int(id)].done, 'description': tasks[int(id)].description}
    return 'Not Found 404'


@app.post('/tasks')
async def create_task(task: Task):
    if tasks:
        tasks[max(tasks) + 1] = task
    else:
        tasks[1] = task
    await logger.info('Создана новая задача')
    return 'task created'


@app.put('/tasks/{id}')
async def change_task(id: int, task: Task):
    if id in tasks:
        tasks[id] = task
        return f'task {id} updated'
    return 'task not found'


@app.delete('/tasks/{id}')
async def del_task(id_task: int):
    if id_task in tasks:
        del tasks[id_task]
        return f"task {id_task} deleted"
    return 'task not found'
