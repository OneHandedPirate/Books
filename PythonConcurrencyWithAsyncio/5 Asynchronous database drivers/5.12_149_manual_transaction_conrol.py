import asyncio
import asyncpg
from asyncpg.transaction import Transaction

from db_config import config


async def main():
    connection = await asyncpg.connect(**config)

    transaction: Transaction = connection.transaction()

    # Start transaction
    await transaction.start()

    try:
        await connection.execute("""insert into brand(brand_name) values(brand_1)""")
        await connection.execute("""insert into brand(brand_name) values(brand_2)""")
    except asyncpg.PostgresError:
        print("Error! Transaction is rolling back")
        await transaction.rollback()
    else:
        print("No errors, transaction is committing")
        await transaction.commit()

    query = """select brand_name from brand where brand_name like 'brand%'"""
    brands = await connection.fetch(query)
    print(brands)

    await connection.close()


asyncio.run(main())
