import time


freqs = {}

with open("googlebooks-eng-all-1gram-20120701-a", encoding="utf-8") as f:
    lines = f.readlines()

    start = time.time()

    for line in lines:
        data = line.split("\t")
        word = data[0]
        count = int(data[1])
        freqs[word] = freqs.get(word, 0) + count

end = time.time()
print(f"{end - start}:.4f")
