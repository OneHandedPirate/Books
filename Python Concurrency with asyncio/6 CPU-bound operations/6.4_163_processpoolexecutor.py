import time
from concurrent.futures import ProcessPoolExecutor


def count(count_to: int) -> int:
    start = time.time()

    count = 0

    while count < count_to:
        count += 1

    print(f"Time to {count_to} count: {time.time() - start}")

    return count


if __name__ == "__main__":
    with ProcessPoolExecutor() as process_pool:
        numbers = [1, 2, 5, 100, 100_000_000]
        for result in process_pool.map(count, numbers):
            print(result)
