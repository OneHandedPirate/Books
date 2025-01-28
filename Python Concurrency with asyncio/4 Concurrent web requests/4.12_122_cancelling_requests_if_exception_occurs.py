import asyncio
import logging

import aiohttp
from utils import async_timed, fetch_status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [
            asyncio.create_task(fetch_status(session, "python://example.com")),
            asyncio.create_task(fetch_status(session, "https://example.com", 3)),
            asyncio.create_task(fetch_status(session, "https://example.com", 3)),
        ]

        done, pending = await asyncio.wait(
            fetchers, return_when=asyncio.FIRST_EXCEPTION
        )

        print(f"Tasks done: {len(done)}")
        print(f"Pending tasks: {len(pending)}")

        for done_task in done:
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error(
                    "Exception occured while requesting", exc_info=done_task.exception()
                )

        for pending_task in pending:
            pending_task.cancel()


asyncio.run(main())
