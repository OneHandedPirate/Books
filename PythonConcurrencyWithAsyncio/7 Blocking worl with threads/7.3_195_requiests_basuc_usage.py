import requests


def get_status_code(url: str) -> int:
    response = requests.get(url)
    return response.status_code


url = "http://example.com"
print(get_status_code(url))
print(get_status_code(url))
