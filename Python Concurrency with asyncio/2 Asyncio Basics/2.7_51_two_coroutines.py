import asyncio
import utils


async def add_one(n: int) -> int:
    return n + 1


async def hello_world_of_morpheus() -> str:
    await utils.delay(1)
    return "Hello, world!"


async def main() -> None:
    message = await hello_world_of_morpheus()
    one_plus_one = await add_one(1)

    print(message, one_plus_one, sep="\n")


asyncio.run(main())
