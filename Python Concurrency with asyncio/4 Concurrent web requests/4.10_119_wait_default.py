import asyncio
import aiohttp
from utils import async_timed, fetch_status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [
            asyncio.create_task(fetch_status(session, 'https://example.com')),
            asyncio.create_task(fetch_status(session, 'https://example.com'))
        ]

        done, pending = await asyncio.wait(fetchers)

        print(f'Tasks done: {len(done)}')
        print(f'Pending tasks: {len(pending)}')

        for done_task in done:
            result = await done_task
            print(result)


asyncio.run(main())
