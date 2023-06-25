# O(n**2)
from random import choice

while True:
    try:
        _max = int(input("Введите число элементов: "))
    except ValueError:
        print("Некорректный ввод!")
        continue
    else:
        break

array = [choice(range(_max * (-1), _max)) for _ in range(_max)]

count = 0


def find_smallest_indx(arr: list) -> int:
    smallest_elem, smallest_indx = arr[0], 0
    for i in range(1, len(arr)):
        global count
        count += 1

        if arr[i] < smallest_elem:
            smallest_elem = arr[i]
            smallest_indx = i
    return smallest_indx


def selection_sort(arr: list) -> list:
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest_indx(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


print(selection_sort(array), count, sep="\n")
