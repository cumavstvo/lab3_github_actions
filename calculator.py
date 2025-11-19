def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Division by zero")
    return a / b


if __name__ == "__main__":
    x = float(input("Введите первое число: "))
    y = float(input("Введите второе число: "))
    print("Сумма:", add(x, y))
    print("Разность:", subtract(x, y))
    print("Произведение:", multiply(x, y))
    try:
        print("Частное:", divide(x, y))
    except ValueError as e:
        print("Ошибка:", e)
