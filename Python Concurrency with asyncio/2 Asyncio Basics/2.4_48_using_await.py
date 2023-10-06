import asyncio


async def add_one(n: int) -> int:
    return n + 1


async def main():
    one_plus_one = await add_one(1)
    two_plus_one = await add_one(2)

    print(one_plus_one, two_plus_one, sep='\n')

asyncio.run(main())
