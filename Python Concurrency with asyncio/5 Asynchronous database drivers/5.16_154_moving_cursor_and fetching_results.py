import asyncpg
import asyncio

from db_config import config


async def main():
    connection = await asyncpg.connect(**config)
    async with connection.transaction():
        query = "SELECT product_id, product_name from product"
        cursor = await connection.cursor(query)
        await cursor.forward(500)
        products = await cursor.fetch(100)
        for product in products:
            print(product)

    await connection.close()


asyncio.run(main())
