import asyncio
import asyncpg
from db_tables import *


async def main():
    config = {
        "host": "localhost",
        "port": 5432,
        "user": "postgres",
        "database": "products",
        "password": "password",
    }

    connection = await asyncpg.connect(**config)
    statements = [
        CREATE_BRAND_TABLE,
        CREATE_PRODUCT_TABLE,
        CREATE_PRODUCT_COLOR_TABLE,
        CREATE_PRODUCT_SIZE_TABLE,
        CREATE_SKU_TABLE,
        SIZE_INSERT,
        COLOR_INSERT,
    ]

    print("Creating products database...")
    for statement in statements:
        status = await connection.execute(statement)
        print(status)

    print("Products database created!")
    await connection.close()


asyncio.run(main())
