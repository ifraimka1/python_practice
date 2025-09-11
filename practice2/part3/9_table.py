# Задача №9
# Вывести таблицу умножения для n

n = int(input("Введите число n: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i} x {j} = {i*j}\t", end="\t")
    print()
