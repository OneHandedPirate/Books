from multiprocessing import Process, Value


def increment_value(shared_int: Value) -> None:
    shared_int.get_lock().acquire()  # acquire resource lock to prevent race condition
    shared_int.value += 1
    shared_int.get_lock().release()  # release resource lock

    # with shared_int.get_lock():  # lock as context manager
    #     shared_int.value += 1


if __name__ == "__main__":
    for _ in range(100):
        integer = Value("i", 0)
        procs = [
            Process(target=increment_value, args=(integer,)),
            Process(target=increment_value, args=(integer,)),
        ]

        [p.start() for p in procs]
        [p.join() for p in procs]

        print(integer.value)
        assert integer.value == 2

# Race condition prevented, but in fact we got synchronous code now
