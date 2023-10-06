import asyncio
from asyncio import AbstractEventLoop
from typing import Any


async def add_one(n: int) -> tuple[int, AbstractEventLoop]:
    loop = asyncio.get_running_loop()
    return n + 1, loop


result = asyncio.run(add_one(2))
result2 = asyncio.run(add_one(4))

print(result[0], result2[0], result[1] == result2[1], result[1] is result2[1])
