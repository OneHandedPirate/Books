import asyncio


async def delay(d: int) -> int:
    print(f'Falling asleep for {d} seconds')
    await asyncio.sleep(d)
    print(f'Sleeping for {d} seconds is over')
    return d
