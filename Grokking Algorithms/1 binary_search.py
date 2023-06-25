# O(log n)

from random import randint


while True:
    try:
        _max = int(input('Максимальное число: '))
    except ValueError:
        print("Invalid input, please try again!")
        continue
    else:
        break


def binary_search(max_num: int) -> tuple[int | None, int]:

    guess_num = randint(0, max_num*2)
    tries = 0

    l, r = 0, max_num

    while l <= r:
        mid = (l + r) // 2

        if mid == guess_num:
            return guess_num, tries
        if mid > guess_num:

            r = mid - 1
            tries += 1
        else:
            l = mid + 1
            tries += 1

    return None, tries


print(binary_search(_max))
