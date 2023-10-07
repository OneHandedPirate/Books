import asyncio

from utils import async_timed


@async_timed()
async def delay(delay_seconds: int) -> int:
    print(f'Sleeping for {delay_seconds} seconds')
    await asyncio.sleep(delay_seconds)
    print(f'I\'m awake from {delay_seconds} seconds sleep')

    return delay_seconds


@async_timed()
async def main():
    task_one = asyncio.create_task(delay(2))
    task_two = asyncio.create_task(delay(3))

    await task_one
    await task_two

asyncio.run(main())
