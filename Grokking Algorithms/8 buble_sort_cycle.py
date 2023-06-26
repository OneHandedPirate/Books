#O(n**2)

from random import choice

while True:
    try:
        _max = int(input("Введите число элементов: "))
    except ValueError:
        print("Некорректный ввод!")
    else:
        break

array = [choice(range(_max * (-1), _max)) for _ in range(_max)]

print(array)

def bubble_sort(array: list) -> list:
    # Если закомментировать эту строку - получится аналог .sort(),
    # если оставить - аналог sorted()
    #array = array.copy()

    _l = len(array) - 1

    while _l >= 2:
        for i in range(_l):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        _l -= 1
    return array


bubble_sort(array)

print(array, sep='\n')
