numbers: list[int] = [1, 2, 3, 4, 5]

def is_even(number):
    return number % 2 == 0

even_numbers: filter = filter(is_even, numbers)

print(list(even_numbers))