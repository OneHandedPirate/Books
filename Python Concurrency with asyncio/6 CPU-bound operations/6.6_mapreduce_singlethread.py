import functools


def map_frequency(text: str) -> dict[str, int]:
    words = text.split()
    word_set = set(words)
    frequencies = {word: words.count(word) for word in word_set}
    return frequencies


def merge_dicts(first: dict[str, int], second: dict[str, int]) -> dict[str, int]:
    merged = first
    for key in second:
        merged[key] = merged.get(key, 0) + second[key]
    return merged


lines = [
    "I know what I know",
    "I know that I know",
    "I don't know much",
    "They don't know much"
]

mapped_result = [map_frequency(line) for line in lines]

for result in mapped_result:
    print(result)

print(functools.reduce(merge_dicts, mapped_result))
