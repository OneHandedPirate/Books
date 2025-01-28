while True:
    try:
        f = int(input("Введите число, факториал которого нужно узнать: "))
        if f >= 999 or f <= 0:
            print("Некорректный ввод")
            continue
    except ValueError:
        print("Некорректный ввод")
    else:
        break


def factorial(num: int) -> int:
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(f))
