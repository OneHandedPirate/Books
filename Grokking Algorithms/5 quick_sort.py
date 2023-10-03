# Average O(n*logn)

from random import choice

while True:
    try:
        _max = int(input("Введите число элементов: "))
    except ValueError:
        print("Некорректный ввод!")
    else:
        break

array = [choice(range(_max * (-1), _max)) for _ in range(_max)]


def quick_sort(array: list) -> list:
    if len(array) < 2:
        return array
    else:
        pivot_indx = len(array)//2
        pivot = array[pivot_indx]
        less = [i for i in (array[:pivot_indx] + array[pivot_indx+1:]) if pivot >= i]
        greater = [i for i in (array[:pivot_indx] + array[pivot_indx+1:]) if pivot < i]

        return quick_sort(less) + [pivot] + quick_sort(greater)


sorted_array = quick_sort(array)

print(array, sorted_array, len(sorted_array), sep='\n')

