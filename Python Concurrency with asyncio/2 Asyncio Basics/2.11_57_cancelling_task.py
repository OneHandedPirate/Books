import asyncio
from asyncio import CancelledError

from utils import delay


async def long_task():
    print("Starting long task")
    return await delay(10)


async def main():
    _long_task = asyncio.create_task(long_task())

    seconds_elapsed = 0

    while not _long_task.done():
        print("Task is not completed, next check after 1 second")
        await asyncio.sleep(1)
        seconds_elapsed += 1

        if seconds_elapsed == 5:
            _long_task.cancel()

    try:
        await _long_task
    except CancelledError:
        print("Long task cancelled")


asyncio.run(main())
