import asyncio
from utils import async_timed, delay


@async_timed()
async def main():
    delay_time = [3, 3, 3]
    tasks = [asyncio.create_task(delay(seconds)) for seconds in delay_time]
    [await task for task in tasks]

asyncio.run(main())

# Took ~ 3 seconds
