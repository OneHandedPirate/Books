import time
import requests
from concurrent.futures import ThreadPoolExecutor


def get_status_code(url: str) -> int:
    response = requests.get(url)
    return response.status_code


start = time.time()

with ThreadPoolExecutor() as pool:
    urls = ["http://example.com" for _ in range(100)]

    for result in pool.map(get_status_code, urls):
        print(result)

    print(f"Elapsed time: {time.time() - start:.5f}")

# 8.43495
