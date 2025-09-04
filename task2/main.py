# С начала суток прошло m минут (0 < m < 24*60). Определить
# целое количество часов
# количество минут, прошедших с последнего часа

def print_time(m):
    hours, minutes = divmod(m, 60)
    print(f"hours = {hours}, minutes = {minutes}")


while True:
    m = int(input("Введите значение m: "))
    print_time(m)

    response = input("Введите y, если хотите ввести другие значения ")
    if response != "y":
        break
