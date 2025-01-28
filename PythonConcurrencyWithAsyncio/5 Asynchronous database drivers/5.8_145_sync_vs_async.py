import asyncio
import asyncpg
from temp import product_query
from db_config import config
from utils import async_timed


async def query_product(pool):
    async with pool.acquire() as connection:
        return await connection.fetchrow(product_query)


@async_timed()
async def query_products_synchronously(pool, queries):
    return [await query_product(pool) for _ in range(queries)]


@async_timed()
async def query_products_asynchronously(pool, queries):
    queries = [query_product(pool) for _ in range(queries)]
    return await asyncio.gather(*queries)


async def main():
    async with asyncpg.create_pool(**config, min_size=6, max_size=6) as pool:
        await query_products_synchronously(pool, 10000)
        await query_products_asynchronously(pool, 10000)


asyncio.run(main())
