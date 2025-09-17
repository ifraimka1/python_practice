def calculate_sum(number):
    if number > 0:
        return number % 10 + calculate_sum(number // 10)
    else:
        return number


def get_number_len(number):
    if number > 0:
        return 1 + get_number_len(number // 10)
    else:
        return 0


number = int(input('Enter a number: '))
number_sum = calculate_sum(number)
number_len = get_number_len(number)
print(f"Sum: {number_sum}, Length: {number_len}")
