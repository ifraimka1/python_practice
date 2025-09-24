from Terminal import Terminal


terminal = Terminal()

while True:
    terminal.display_menu()
    option = int(input('Введите номер пиццы для добавления в заказ: '))
    terminal.process(option)
