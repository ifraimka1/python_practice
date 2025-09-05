# Вывести подстроки для "объектно-ориентированный"

string = "объектно-ориентированный"
output_array = []
first, second = string.split("-")
# объект
output_array.append(first[0:6])
# ориентир
output_array.append(second[0:8])
# тир
output_array.append(output_array[1][5:8])
# кот
output_array.append(first[6] + first[0] + first[5])
# рента
output_array.append(second[1] + second[3:6] + second[10])

for item in output_array:
    print(item)
