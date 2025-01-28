import time
import requests


def read_example() -> None:
    res = requests.get("http://example.com")
    print(res.status_code)


sync_start = time.time()

read_example()
read_example()

sync_end = time.time()

print(f"Sync running took {sync_end - sync_start:0.4f} seconds")
