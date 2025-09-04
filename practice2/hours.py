# С начала суток прошло m минут (0 < m < 24*60). Определить
# целое количество часов
# количество минут, прошедших с последнего часа

def print_time(m):
    hours, minutes = divmod(m, 60)
    print(f"hours = {hours}, minutes = {minutes}")


while True:
    m = input("Введите значение m: ")
    if m == "exit":
        break

    print_time(int(m))
