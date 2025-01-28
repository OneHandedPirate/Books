import asyncpg
import asyncio
import asyncpg

from db_config import config


async def main():
    connection = await asyncpg.connect(**config)

    query = "SELECT product_id, product_name FROM product"
    async with connection.transaction():
        async for product in connection.cursor(query):
            print(product)

    await connection.close()


asyncio.run(main())
