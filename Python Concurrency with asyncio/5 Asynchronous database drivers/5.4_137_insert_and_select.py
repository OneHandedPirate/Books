import asyncio
import asyncpg
from asyncpg import Record


async def main():
    config = {
        'host': 'localhost',
        'port': 5432,
        'user': 'postgres',
        'database': 'products',
        'password': 'password'
    }

    connection = await asyncpg.connect(**config)
    await connection.execute("INSERT INTO brand (brand_name) VALUES ('Levis'), ('SEVEN');")

    brand_query = 'SELECT brand_id, brand_name FROM brand'
    results: list[Record] = await connection.fetch(brand_query)

    for brand in results:
        print(f'id: {brand["brand_id"]}, name: {brand["brand_name"]}')
    await connection.close()


asyncio.run(main())
