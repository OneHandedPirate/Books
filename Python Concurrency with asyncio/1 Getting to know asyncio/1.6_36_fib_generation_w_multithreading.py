import threading
import time


def print_fib(number: int) -> None:
    def fib(n: int) -> int:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)

    print(f"fib({number}) equals {fib(number)}")


def fibs_with_threads():
    thread40 = threading.Thread(target=print_fib, args=(40,))
    thread41 = threading.Thread(target=print_fib, args=(41,))

    thread40.start()
    thread41.start()

    thread40.join()
    thread41.join()


start = time.time()

fibs_with_threads()

end = time.time()

# No advantage over sync fib_generator (even more time to compute)
print(f"Running time with multithreading is {end - start:.4f} sec.")
