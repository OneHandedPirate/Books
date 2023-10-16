import asyncio
import functools
import time
from typing import Callable, Any

from aiohttp import ClientSession


async def delay(d: int) -> int:
    print(f'Falling asleep for {d} seconds')
    await asyncio.sleep(d)
    print(f'Sleeping for {d} seconds is over')
    return d


def async_timed():
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            print(f'Calling {func} with arguments {args} {kwargs}')
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f'{func} took {total:.4f} seconds')
        return wrapped
    return wrapper


async def fetch_status(session: ClientSession, url: str, delay: int = 0) -> int:
    if delay:
        await asyncio.sleep(delay)
    async with session.get(url) as result:
        return result.status

