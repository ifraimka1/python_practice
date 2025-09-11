# Задача №9
# Вывести таблицу умножения для n

n = int(input("Введите число n: "))

i = j = 1
for i in range(n + 1):
    for j in range(n + 1):
        print(f"{i} x {j} = {i*j}\t", end="\t")
    print()
