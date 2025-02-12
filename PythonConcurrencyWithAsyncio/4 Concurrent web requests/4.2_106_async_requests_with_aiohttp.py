import asyncio
import aiohttp
from aiohttp import ClientSession
from utils import async_timed


@async_timed()
async def fetch_status(session: ClientSession, url: str) -> int:
    async with session.get(url) as result:
        return result.status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        url = "https://example.com"
        status = await fetch_status(session, url)
        print(f"Status code for {url} is {status}")


asyncio.run(main())
