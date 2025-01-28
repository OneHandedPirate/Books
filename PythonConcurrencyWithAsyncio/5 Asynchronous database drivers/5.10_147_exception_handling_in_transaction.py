import asyncio
import logging
import asyncpg

from db_config import config


async def main():
    connection = await asyncpg.connect(**config)
    try:
        async with connection.transaction():
            insert_brand = """INSERT INTO brand VALUES(9999, 'bug_brand')"""
            await connection.execute(insert_brand)
            await connection.execute(insert_brand)
    except Exception:
        logging.exception("Error occurred while inserting brand")
    finally:
        query = """SELECT brand_name FROM brand WHERE brand_name LIKE 'big_%'"""
        brands = await connection.fetch(query)
        print(f"Query result: {brands}")
        await connection.close()


asyncio.run(main())
