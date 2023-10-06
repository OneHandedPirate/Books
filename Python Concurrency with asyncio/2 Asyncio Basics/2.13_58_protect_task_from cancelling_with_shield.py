import asyncio
from utils import delay


async def main():
    task = asyncio.create_task(delay(10))

    try:
        result = await asyncio.wait_for(asyncio.shield(task), 5)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print('Task is running for over 5 seconds')
        result = await task
        print(result)


asyncio.run(main())
