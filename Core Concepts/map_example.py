numbers: list[int] = [1, 2, 3, 4, 5]

def square(number):
    return number ** 2

squared_numbers = map(square, numbers)

print(list(squared_numbers))