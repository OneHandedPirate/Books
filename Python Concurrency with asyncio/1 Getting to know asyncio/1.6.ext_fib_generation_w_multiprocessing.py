import multiprocessing
import time


threads = int(input('How many threads does your processor have?\n'))


def print_fib(number: int) -> None:
    def fib(n: int) -> int:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)

    print(f'fib({number}) equals {fib(number)}')


def fib_with_processes():
    processes = [multiprocessing.Process(target=print_fib, args=(40,)) for _ in range(threads-1)]

    for process in processes:
        process.start()

    for process in processes:
        process.join()


start = time.time()

fib_with_processes()

end = time.time()


print(f'Running time with multithreading is {end - start:.4f} sec.')