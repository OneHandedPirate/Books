from threading import RLock


class IntListThreadsafe:
    def __init__(self, wrapped_list: list[int]):
        self._list = wrapped_list
        self._lock = RLock()

    def indices_of(self, to_find: int) -> list[int]:
        with self._lock:
            enumerator = enumerate(self._list)
            return [i for i, v in enumerator if v == to_find]

    def find_and_replace(self, to_replace: int, replacement: int) -> None:
        with self._lock:
            indices = self.indices_of(to_replace)
            for index in indices:
                self._list[index] = replacement

    def __repr__(self):
        return f"IntListThreadsafe({self._list})"


threadsafe_list = IntListThreadsafe([1, 2, 3, 1, 5])
threadsafe_list.find_and_replace(1, 0)
print(threadsafe_list)