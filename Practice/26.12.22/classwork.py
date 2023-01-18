import asyncio
from time import monotonic


async def coro(num):
    print(f'Coro #{num} started')
    await asyncio.sleep(num)
    print(f'Coro #{num} is done')


async def main():
    tasks = [asyncio.create_task(coro(i), name=str(i)) for i in range(4)]
    done, pending = await asyncio.wait(tasks, timeout=3)
    done_names = [task.get_name() for task in done]
    pending_names = [task.get_name() for task in pending]
    print(f'Done: {done_names}')
    print(f'Pending: {pending_names}')

start = monotonic()
asyncio.run(main())
