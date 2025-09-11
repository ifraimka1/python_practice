# Требования к данным:
# - 3+ объекта
# - 5+ атрибутов
# - 3+ различных типа
# - 1+ атрибут типа list
#
# Вариант 2
# Финтес-центр: терминал с информацией о клубных картах

data = [
    {
        "name": "Соломонов Ифраим",
        "age": 22,
        "height": 185,
        "weight": 71.3,
        "sex": "Мужской",
        "limitless": False,
        "sessions": 4,
        "goals": ["Ноги", "Пресс"],
    },
    {
        "name": "Краснопольская Екатерина",
        "age": 25,
        "height": 170,
        "weight": 51.4,
        "sex": "Женский",
        "limitless": True,
        "goals": ["Спина", "Плечи"],
    },
    {
        "name": "Смирнов Павел",
        "age": 30,
        "height": 180,
        "weight": 130.7,
        "sex": "Мужской",
        "limitless": False,
        "sessions": 4,
        "goals": ["Похудение"],
    }
]

print("Данные о клиентах фитнесс-центра ({}):\n".format(len(data)))

for i, item in enumerate(data):
    print(i + 1)
    print("Имя: {}".format(item["name"]))
    print("Возраст: {}".format(item["age"]))
    print("Рост: {}".format(item["height"]))
    print("Вес: {}".format(item["weight"]))
    print("Пол: {}".format(item["sex"]))
    if item["limitless"]:
        print("Безлимитный тариф")
    else:
        print("Осталось занятий: {}".format(item["sessions"]))
    print("Цели: {}\n".format(item["goals"]))
