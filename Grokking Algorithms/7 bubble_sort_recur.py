# O(n**2)

from random import choice

while True:
    try:
        _max = int(input("Введите число элементов: "))
    except ValueError:
        print("Некорректный ввод!")
    else:
        break

array = [choice(range(_max * (-1), _max)) for _ in range(_max)]


def bubble_sort(array: list) -> list:
    if len(array) < 2:
        return array
    for idx in range(len(array)-1):
        if array[idx] > array[idx+1]:
            array[idx], array[idx+1] = array[idx+1], array[idx]
    return bubble_sort(array[:-1]) + [array[-1]]


print(array, bubble_sort(array), array, sep='\n')