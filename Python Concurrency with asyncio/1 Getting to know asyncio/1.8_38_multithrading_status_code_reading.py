import time
import threading
import requests


def read_example() -> None:
    res = requests.get('http://example.com')
    print(res.status_code)


thread_1 = threading.Thread(target=read_example)
thread_2 = threading.Thread(target=read_example)

start_time = time.time()

thread_1.start()
thread_2.start()

print('All threads are running!')

thread_1.join()
thread_2.join()

end_time = time.time()

# Approximately 2 times faster than sync version
print(f'Multithreading running took {end_time-start_time:.4f} seconds')
