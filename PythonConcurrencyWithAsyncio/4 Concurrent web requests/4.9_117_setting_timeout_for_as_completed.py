import asyncio
import aiohttp
from utils import async_timed, fetch_status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [
            fetch_status(session, "https://example.com", 1),
            fetch_status(session, "https://example.com", 1),
            fetch_status(session, "https://example.com", 10),
        ]

        for done_task in asyncio.as_completed(fetchers, timeout=2):
            try:
                result = await done_task
                print(result)
            except asyncio.TimeoutError:
                print("Timeout!!!")

        for task in asyncio.all_tasks():
            print(task)


asyncio.run(main())
