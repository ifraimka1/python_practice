# Задача №2.
# Решить квадратное уравнение для вещественных a, b и c

def calculate_d(a, b, c):
    d = b**2 - 4 * a * c
    if d < 0:
        return "Решений нет :("
    elif d == 0:
        x = -b / (2 * a)
        x = round(x)
        return f"x = {x}"
    else:
        x1 = (-b - d ** 0.5) / (2 * a)
        x2 = (-b + d ** 0.5) / (2 * a)
        x1 = round(x1, 1)
        x2 = round(x2, 1)
        return f"x1 = {x1} x2 = {x2}"


print("Решение кв. уравнения | ax^2 + bx + c = 0")

while True:
    a = float(input("Введите значение a: "))
    b = float(input("Введите значение b: "))
    c = float(input("Введите значение c: "))
    print(calculate_d(a, b, c))

    response = input("Введите y, если хотите ввести другие значения ")
    if response != "y":
        break
