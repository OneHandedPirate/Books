import asyncio

from utils import delay


def call_later():
    print("I will be called later")


async def main():
    loop = asyncio.get_running_loop()
    loop.call_soon(call_later)
    await delay(1)


asyncio.run(main())
