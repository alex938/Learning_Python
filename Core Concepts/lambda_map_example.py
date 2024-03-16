numbers = ["1", "2", "3"]
numbers = list(map(int, numbers))
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

numbers = ["1", "2", "3"]
numbers = list(map(int, numbers))
incremented_numbers = list(map(lambda x: x + 10, numbers))
print(incremented_numbers)

numbers = ["1", "2", "3"]
float_numbers = list(map(float, numbers))
print(float_numbers)