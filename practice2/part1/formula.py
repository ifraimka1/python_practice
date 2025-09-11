# Задача №2 - вычислить значение выражения
import math


def calculate(x, y, z):
    result = (x**5 + 7) / (6 * y)  # Верхняя дробь
    result = math.pow(result, 1/3)  # Извлекаем корень
    result /= 7 - z % y  # Делим на знаменатель
    result = round(result, 3)

    return result


while True:
    x = int(input("Введите значение x: "))
    y = int(input("Введите значение y: "))
    z = int(input("Введите значение z: "))
    print(calculate(x, y, z))

    response = input("Введите y, если хотите продолжить: ")
    if response != "y":
        break
