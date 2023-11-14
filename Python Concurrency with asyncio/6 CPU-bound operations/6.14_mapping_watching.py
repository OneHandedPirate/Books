from concurrent.futures import ProcessPoolExecutor
import asyncio
import functools
from multiprocessing import Value

map_progress: Value


def init(progress: Value):
    global map_progress
    map_progress = progress


def map_frequencies(chunk: list[str]) -> dict[str, int]:
    counter = {}
    for line in chunk:
        word, _, count, _ = line.split("\t")
        counter[word] = counter.get(word, 0) + int(count)

    with map_progress.get_lock():
        map_progress.value += 1
    return counter


def partition(data: list, chunk_size: int) -> list:
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]


def merge_dicts(first: dict[str, int], second: dict[str, int]) -> dict[str, int]:
    merged = first
    for key in second:
        merged[key] = merged.get(key, 0) + second[key]
    return merged


async def progress_reported(total_partitions: int):
    while map_progress.value < total_partitions:
        print(f"Mapping progress: {map_progress.value}/{total_partitions}")
        await asyncio.sleep(1)


async def main(partition_size: int):
    global map_progress

    with open("googlebooks-eng-all-1gram-20120701-a", encoding="utf-8") as f:
        content = f.readlines()
        loop = asyncio.get_running_loop()
        tasks = []
        map_progress = Value('i', 0)

        with ProcessPoolExecutor(initializer=init, initargs=(map_progress,)) as pool:
            total_partitions = len(content) // partition_size
            reporter = asyncio.create_task(progress_reported(total_partitions))

            for chunk in partition(content, partition_size):
                tasks.append(
                    loop.run_in_executor(pool,functools.partial(map_frequencies, chunk))
                )

            counters = await asyncio.gather(*tasks)

            await reporter

            final_results = functools.reduce(merge_dicts, counters)

            print(f'Aardvark count: {final_results["Aardvark"]}')


if __name__ == "__main__":
    asyncio.run(main(70_000))
