from time import time, sleep
from multiprocessing import Pool


def say_hello(name: str) -> str:
    sleep(5)
    return f'Hello, {name}'


if __name__ == '__main__':
    with Pool() as process_pool:
        start = time()

        hi_jeff = process_pool.apply_async(say_hello, args=('Jeff',))
        hi_john = process_pool.apply_async(say_hello, args=('John',))

        print(hi_jeff.get(), hi_john.get(), f'Time: {time() - start}', sep='\n')

# This time processes run truly parallel, but if hi_jeff would take 10s and
# hi_john would take 1s we should have waited for hi_jeff to see result from hi_john
