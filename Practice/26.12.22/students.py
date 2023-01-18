import asyncio
from random import randrange


# async def hello():
#     await asyncio.sleep(2)
#     print('Hello')
#     return 'Hello'

# async def world():
#     await asyncio.sleep(3)
#     print('World')
#     raise ValueError

# async def main():
#     async with asyncio.TaskGroup() as tg:
#         tg.create_task(hello())
#         tg.create_task(world())

# async def main():
#     print(await asyncio.gather(hello(), world(), return_exceptions=True))

# asyncio.run(main())

# Ball moves evenly and then moves with acceleration


def proc(pracent):
    return pracent > randrange(100)


class A:
    @staticmethod
    async def task_1(data):
        await asyncio.sleep(3)
        return data + ' task_1 completed'

    @staticmethod
    async def task_2(data):
        await asyncio.sleep(4)
        return data + 100

    @classmethod
    async def main(cls, data):
        return await asyncio.gather(cls.task_1(data), cls.task_2(data), return_exceptions=True)


async def work():
    print(await (A.main('Coroutine')))


# print(*(A, A.task_1, A.main, A.task_2))
# asyncio.run(work())

class Listik:
    LOCATIONS = {'Деканат': 3, 'Библиотека': 2, 'Студ отдел кадров': 4, 'Студ городок': 1}

    @classmethod
    async def task_1(cls, name, location):
        await asyncio.sleep(cls.LOCATIONS.get(location))
        if proc(70):
            print(f'Студент {name} получил подпись {location}')
        else:
            print(f"Студент {name} не забрал подпись {location}")

    @classmethod
    async def main(cls, name):
        tasks = [asyncio.create_task(cls.task_1(name, location)) for location in cls.LOCATIONS.keys()]
        done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_EXCEPTION)
        for task in pending:
            task.cancel()
        return len(done) == 4


class Student:

    def __init__(self, name):
        self.name = name

    async def work(self):
        lst = await Listik.main(self.name)
        if lst:
            print(f'Все подписи собраны у {self.name}')
        else:
            print(f'Что-то пошло не так у {self.name}')


STUDENTS = [
    'Aboba',
    'Biba',
    'Cus-cus',
    'Kokos'
]


async def st():
    await asyncio.gather(*[Student(student).work() for student in STUDENTS])


asyncio.run(st())
