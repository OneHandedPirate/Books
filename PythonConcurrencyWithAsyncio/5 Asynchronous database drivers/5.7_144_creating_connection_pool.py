import asyncio
import asyncpg
from temp import product_query
from db_config import config


async def query_product(pool):
    async with pool.acquire() as connection:
        return await connection.fetchrow(product_query)


async def main():
    async with asyncpg.create_pool(**config, min_size=6, max_size=6) as pool:
        await asyncio.gather(query_product(pool), query_product(pool))


asyncio.run(main())
