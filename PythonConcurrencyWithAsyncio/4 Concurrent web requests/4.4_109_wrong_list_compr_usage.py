import asyncio
from utils import async_timed, delay


@async_timed()
async def main():
    delay_time = [3, 3, 3]
    [await asyncio.create_task(delay(seconds)) for seconds in delay_time]


asyncio.run(main())

# Took ~9 seconds to complete since we await every time we create a task
