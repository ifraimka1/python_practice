import random
from Order import Order
import Pizza


class Terminal:
    menu = [
        Pizza.Pepperoni(),
        Pizza.BBQ(),
        Pizza.Seafood()
    ]

    def __init__(self):
        self.order = Order()
        self.show_menu = False

    def display_menu(self):
        for i, pizza in self.menu:
            print(f'{i}.' + pizza)
        if self.order.ordered_pizzas:
            print(f'{len(self.menu)}. Оплатить заказ - {self.order.sum()}')
            print(f'{len(self.menu) + 1}. Отменить заказ - {self.order.sum()}')

    def process(self, number: int):
        if number < len(self.menu):
            self.order.add_pizza(self.menu[number])
        elif number == len(self.menu):
            self.accept_payment()
            self.order = Order()
        elif number == len(self.menu) + 1:
            self.order = Order()
            print('Заказ отменён')

    def accept_payment(self):
        print('Обработка платежа')
        payment_status = random.getrandbits(1)
        if (payment_status):
            print('Оплата прошла успешно')
            self.order.execute()
        else:
            print('Оплата не прошла, попробуйте снова')
