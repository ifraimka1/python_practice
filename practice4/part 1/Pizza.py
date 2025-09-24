class Pizza:
    template_name = "Пицца"
    template_dough = "Тесто"
    template_topping = "Соус"
    template_filling = ['Сыр']
    price = 299.9

    def __init__(self):
        self.name = f"{Pizza.template_name} стандартная"
        self.dough = f"{Pizza.template_dough} стандартное"
        self.topping = f"{Pizza.template_topping} томатный"
        self.filling = Pizza.template_filling

    def __str__(self):
        output = f'{self.name}\n'
        output += f'Цена: {self.price}\n'
        output += f'Состав: Тесто {self.dough}, Соус {self.name}'
        output.join(map(lambda x: ', ' + x, self.filling))
        return output

    def prepare(self):
        print(f'Мажем {self.topping} на {self.dough}, добавляем '
              .join(map(lambda x: ', ' + x, self.filling)))

    def bake(self):
        print('Печём')

    def cut(self):
        print('Режем')

    def pack(self):
        print('Упаковываем')


class Pepperoni(Pizza):
    def __init__(self):
        super().__init__()
        self.name = f"{Pizza.template_name} Пепперони"
        self.dough = f"{Pizza.template_dough} стандартное"
        self.topping = f"{Pizza.template_topping} томатный"
        self.filling = Pizza.template_filling + ['Пепперони']
        self.price = super().price + 49.9


class BBQ(Pizza):
    def __init__(self):
        super().__init__()
        self.name = f"{Pizza.template_name} Барбекю"
        self.dough = f"{Pizza.template_dough} стандартное"
        self.topping = f"{Pizza.template_topping} барбекю"
        self.filling = (Pizza.template_filling +
                        ['Пепперони', 'Курица', 'Бекон', 'Томат'])
        self.price = super().price + 199.9


class Seafood(Pizza):
    def __init__(self):
        super().__init__()
        self.name = f"{Pizza.template_name} Дары моря"
        self.dough = f"{Pizza.template_dough} тонкое"
        self.topping = f"{Pizza.template_topping} альфредо"
        self.filling = (Pizza.template_filling +
                        ['Креветка', 'Маслины', 'Мидии'])
        self.price = super().price + 399.9
