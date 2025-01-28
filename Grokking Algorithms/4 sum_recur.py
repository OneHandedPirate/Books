from random import choice

while True:
    try:
        _max = int(input("Введите число элементов: "))
    except ValueError:
        print("Некорректный ввод!")
    else:
        break

array = [choice(range(_max * (-1), _max)) for _ in range(_max)]


def custom_sum(array: list) -> int:
    return 0 if len(array) == 0 else array[0] + custom_sum(array[1:])


def custom_elems(array: list) -> int:
    return 0 if len(array) == 0 else 1 + custom_elems(array[1:])


print(array, custom_sum(array), custom_elems(array), sep="\n")
