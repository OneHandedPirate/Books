import asyncio
import logging

import aiohttp
from utils import async_timed, fetch_status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        good_request = fetch_status(session, 'https://example.com')
        bad_request = fetch_status(session, 'python://example.com')

        fetchers = [asyncio.create_task(good_request), asyncio.create_task(bad_request)]

        done, pending = await asyncio.wait(fetchers)

        print(f'Tasks done: {len(done)}')
        print(f'Pending tasks: {len(pending)}')

        for done_task in done:
            # result = await done_task exception
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error("Exception occured while requesting",
                              exc_info=done_task.exception())


asyncio.run(main())
