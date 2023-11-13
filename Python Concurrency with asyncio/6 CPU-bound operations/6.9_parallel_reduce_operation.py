import asyncio
import concurrent.futures
import functools
import time


async def reduce(loop, pool, counters: list, chunk_size: int) -> dict[str, int]:
    chunks: list[list[dict]] = list(partition(counters, chunk_size))
    reducers = []
    while len(chunks[0]) > 1:
        for chunk in chunks:
            reducer = functools.partial(functools.reduce, merge_dicts, chunk)
            reducers.append(loop.run_in_executor(pool, reducer))
        reducer_chunks = await asyncio.gather(*reducers)
        chunks = list(partition(reducer_chunks, chunk_size))
        reducers.clear()
    return chunks[0][0]


def partition(data: list, chunk_size: int) -> list:
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]


def map_frequencies(chunk: list[str]) -> dict[str, int]:
    counter = {}
    for line in chunk:
        word, _, count, _ = line.split("\t")
        counter[word] = counter.get(word, 0) + int(count)
    return counter


def merge_dicts(first: dict[str, int], second: dict[str, int]) -> dict[str, int]:
    merged = first
    for key in second:
        merged[key] = merged.get(key, 0) + second[key]
    return merged


async def main(partition_size: int):
    with open("googlebooks-eng-all-1gram-20120701-a", encoding="utf-8") as f:
        content = f.readlines()
        loop = asyncio.get_running_loop()
        tasks = []
        start = time.time()

        with concurrent.futures.ProcessPoolExecutor() as pool:
            for chunk in partition(content, partition_size):
                tasks.append(
                    loop.run_in_executor(
                        pool,
                        functools.partial(map_frequencies, chunk)
                    )
                )
            intermediate_results = await asyncio.gather(*tasks)
            final_result = await reduce(loop, pool, intermediate_results, 500)

            print(f"Aardvark count is: {final_result['Aardvark']}")

            print(f'Time elapsed: {time.time() - start:.4f}')


if __name__ == '__main__':
    asyncio.run(main(70_000))
