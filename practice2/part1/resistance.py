# Вычислить общее сопротивление цепи их 2-х последовательных проводников

while True:
    r1 = float(input("Введите значение r1: "))
    r2 = float(input("Введите значение r2: "))
    print(r1 + r2)

    response = input("Введите 'y', если хотите продолжить: ")
    if response != "y":
        break
