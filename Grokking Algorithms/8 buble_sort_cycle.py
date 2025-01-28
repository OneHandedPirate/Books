# O(n**2)
from time import time
from random import choice, randint

while True:
    try:
        _max = int(input("Введите число элементов: "))
    except ValueError:
        print("Некорректный ввод!")
    else:
        break

arr = [choice(range(_max * (-1), _max)) for _ in range(_max)]

print(arr)


def bubble_sort(array: list, save_original: bool = True) -> list:
    if save_original:
        array = array.copy()

    _l = len(array) - 1

    while _l:
        for i in range(_l):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        _l -= 1
    return array


sorted_list = bubble_sort(arr, True)

print(arr, sorted_list, sep="\n")

start_bubble = time()

m = 0


def bubble_sort(array: list, in_place: bool = True) -> list:
    temp = array if in_place else array.copy()

    length = len(temp) - 1
    while length:
        for i in range(length):
            if temp[i] > temp[i + 1]:
                temp[i], temp[i + 1] = temp[i + 1], temp[i]
            global m
            m += 1
        length -= 1
    return None if in_place else temp


new_list = [randint(-100, 100) for _ in "1" * 1000]
print(new_list)
bubble_sort(new_list)

print(
    f"Время на пузырьковую сортировку: {time() - start_bubble:.2f}. Операций: {m}",
    sep="\n",
)

print(new_list)
