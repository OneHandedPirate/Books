import asyncio
from asyncio.events import AbstractEventLoop
from concurrent.futures import ProcessPoolExecutor
from functools import partial
from typing import Callable


def count(count_to: int) -> int:
    counter = 0
    while counter < count_to:
        counter += 1
    return counter


async def main():
    with ProcessPoolExecutor() as pool:
        loop: AbstractEventLoop = asyncio.get_running_loop()
        nums = [1, 3, 5, 22, 100_000_000]
        calls: list[partial[Callable, int]] = [partial(count, num) for num in nums]

        call_coros = []

        for call in calls:
            call_coros.append(loop.run_in_executor(pool, call))

        results = await asyncio.gather(*call_coros)

        for res in results:
            print(res)

if __name__ == "__main__":
    asyncio.run(main())
