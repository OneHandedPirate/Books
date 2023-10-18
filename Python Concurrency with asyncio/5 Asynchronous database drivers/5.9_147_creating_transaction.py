import asyncio
import asyncpg

from db_config import config


async def main():
    connection = await asyncpg.connect(**config)

    async with connection.transaction():
        await connection.execute("INSERT INTO brand(brand_name)"
                                 "VALUES ('brand_1')")
        await connection.execute("INSERT INTO brand(brand_name)"
                                 "VALUES ('brand_2')")

    query = """SELECT brand_name FROM brand WHERE brand_name ILIKE 'brand%'"""
    brands = await connection.fetch(query)

    print(brands)

    await connection.close()
    
asyncio.run(main())
