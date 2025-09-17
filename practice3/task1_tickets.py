# Задание 1
# Вывести все счастливые номера билетов в диапазоне от a до b.
# У счастливого номера количество четных цифр равно количеству нечетных

import math


def is_happy_number(number):
    number_len = round(math.log10(number)) + 1
    even_count = 0
    odd_count = 0

    # Кол-во цифр должно быть четным
    if number_len % 2 != 0:
        return False

    for i in range(number_len):
        digit = number % 10

        if digit % 2 == 0:
            even_count += 1
            if even_count > number_len // 2:
                return False
        else:
            odd_count += 1
            if odd_count > number_len // 2:
                return False

        number = number // 10

    return True


a = int(input('Enter a: '))
b = int(input('Enter b: '))

for i in range(a, b + 1):
    if is_happy_number(i):
        print(i)
