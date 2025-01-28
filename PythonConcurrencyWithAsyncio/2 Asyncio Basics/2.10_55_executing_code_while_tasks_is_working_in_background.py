import asyncio
from utils import delay


async def hello_every_second():
    for i in range(2):
        await asyncio.sleep(1)
        print("While i'm waiting another park of the code is executing")


async def main():
    first_delay = asyncio.create_task(delay(3))
    second_delay = asyncio.create_task(delay(3))

    await hello_every_second()
    await first_delay
    await second_delay


asyncio.run(main())
