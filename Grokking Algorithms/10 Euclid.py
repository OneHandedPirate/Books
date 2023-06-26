while True:
    try:
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
    except ValueError:
        print("Некорректный ввод")
    else:
        break


def euclid(a, b):
    if a < b:
        a, b = b, a
    while True:
        if a % b == 0:
            return b
        a, b = b, a % b


print(euclid(a, b))