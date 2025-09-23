import Pizza


class Order:
    counter = 0

    def __init__(self):
        Order.counter += 1
        self.ordered_pizzas = []

    def __str__(self):
        output = "Текущий заказ: "
        if self.ordered_pizzas:
            for pizza in self.ordered_pizzas:
                output += f"{pizza.name} - {pizza.price} руб.\n"
        else:
            output += 'пуст'
        return output

    def add_pizza(self, pizza: Pizza):
        self.ordered_pizzas.append(pizza)

    def sum(self):
        total = 0
        for pizza in self.ordered_pizzas:
            total += pizza.price
        return total

    def execute(self):
        for pizza in self.ordered_pizzas:
            pizza.prepare()
            pizza.bake()
            pizza.cut()
            pizza.pack()
