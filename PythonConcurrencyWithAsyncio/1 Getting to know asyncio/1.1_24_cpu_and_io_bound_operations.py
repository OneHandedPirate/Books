import requests

response = requests.get("https:/ / www .example .com")  # I/O-bound

items = response.headers.items()

headers = [f"{key}: {header}" for key, header in items]  # CPU-bound

formatted_headers = "\n".join(headers)  # CPU bound

with open("headers.txt", "w") as file:
    file.write(formatted_headers)  # I/O-bound
