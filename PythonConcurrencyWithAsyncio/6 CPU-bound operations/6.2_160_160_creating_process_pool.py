from time import time, sleep
from multiprocessing import Pool


def say_hello(name: str) -> str:
    sleep(5)
    return f"Hello, {name}"


if __name__ == "__main__":
    with Pool() as process_pool:
        start = time()

        hi_jeff = process_pool.apply(say_hello, args=("Jeff",))
        hi_john = process_pool.apply(say_hello, args=("John",))

        print(hi_jeff, hi_john, f"Time: {time() - start}", sep="\n")

# Every time program addresses apply method it blocks execution.
