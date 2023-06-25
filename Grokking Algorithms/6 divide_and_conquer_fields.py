while True:
    try:
        l = int(input("Введите длинну поля: "))
        w = int(input("Введите ширину поля: "))
    except ValueError:
        print("Некорректный ввод")
    else:
        break


def max_square_divide(length: int, width: int) -> int:
    if length < width:
        length, width = width, length
    if length % width == 0:
        return width
    return max_square_divide(length % width, width)


print(max_square_divide(l, w))