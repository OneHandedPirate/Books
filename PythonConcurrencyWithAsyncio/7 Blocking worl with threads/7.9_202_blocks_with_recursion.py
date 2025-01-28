from threading import Lock, Thread, RLock


# list_lock = Lock()
list_lock = RLock()


def sum_list(lst: list[int]) -> int:
    print("Awaiting lock")

    with list_lock:
        print("Acquired lock")

        if not len(lst):
            print("List is empty. Summing complete")
            return 0

        head, *tail = lst
        print("Summing the rest of list")
        return head + sum_list(tail)


thread = Thread(target=sum_list, args=([1, 2, 3, 4, 5, 6, 7],))
thread.start()
thread.join()

# Lock - Программа зависнет при попытке повторного захвата блокировки
# RLock - Программа отработает до конца т.к. RLock - реентерабельная блокировка