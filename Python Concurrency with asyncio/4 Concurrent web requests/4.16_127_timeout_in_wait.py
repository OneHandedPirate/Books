import asyncio

import aiohttp
from utils import async_timed, fetch_status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        url = 'https://example.com'
        fetchers = [
            asyncio.create_task(fetch_status(session, url)),
            asyncio.create_task(fetch_status(session, url)),
            asyncio.create_task(fetch_status(session, url, 3)),
        ]

        # after timeout the tasks don't raise any exceptions if they are still running unlike in wait_for or as_competed
        done, pending = await asyncio.wait(fetchers, timeout=1)

        print(f'Tasks done: {len(done)}')
        print(f'Pending tasks: {len(pending)}')

        for done_task in done:
            print(await done_task)

        for pending_task in pending:
            print(f'Result of task that was still pending when reached timeout: {await pending_task}')

asyncio.run(main())
