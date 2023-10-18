import asyncio
import asyncpg
import logging

from db_config import config


async def main():
    connection = await asyncpg.connect(**config)

    async with connection.transaction():
        await connection.execute("""INSERT INTO brand(brand_name) VALUES('my_new_brand')""")

        try:
            async with connection.transaction():
                await connection.execute("""INSERT INTO product_color VALUES(1, 'black')""")
        except Exception as ex:
            logging.exception('Error while inserting product color is ignored', exc_info=ex)

    await connection.close()


asyncio.run(main())

# Parent transaction will be executed, while nested transaction will be rolled back.
