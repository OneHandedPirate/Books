import asyncio
from utils import delay


async def main():
    results = await asyncio.gather(delay(3), delay(1))
    print(results)  # [3, 1] as they passed to gather


asyncio.run(main())
