import asyncio
import asyncpg
from random import sample
from db_config import config


def load_common_words() -> list[str]:
    with open('common_words.txt') as common_words:
        return [word.strip('\n') for word in common_words.readlines()]


def generate_brand_names(words: list[str]) -> list[tuple[str,]]:
    return [(words[index],) for index in sample(range(100), 100)]


async def insert_brands(common_words, connection) -> int:
    brands = generate_brand_names(common_words)
    insert_brands = "INSERT INTO brand (brand_name) VALUES($1)"
    return await connection.executemany(insert_brands, brands)


async def main():
    common_words = load_common_words()
    connection = await asyncpg.connect(**config)
    await insert_brands(common_words, connection)


asyncio.run(main())
