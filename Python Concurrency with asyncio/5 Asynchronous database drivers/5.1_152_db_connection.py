import asyncio
import asyncpg


async def main():
    config = {
        "host": "localhost",
        "port": 5432,
        "user": "postgres",
        "password": "password",
    }

    connection = await asyncpg.connect(**config)
    version = connection.get_server_version()
    print(f"Connection established! Postgres version: {version}")

    await connection.close()


asyncio.run(main())
