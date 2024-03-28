cats = ["Frank", "Jess", "Phil"]

newlist = [(i, len(i)) for i in cats if len(i) > 4]

print(newlist)

newlist = [(i, ln) for i in cats if (ln:=len(i)) > 4]

print(newlist)

#example 2

users: dict[int, str] = {0: 'Bob', 1: 'Roger'}

if user := users.get(3): print(f"{user} exists!")
else: print("User does not exist!")

#example 3

def get_text_info(text: str) -> dict:
    return {'words': (words := text.split()),
            'word_count': len(words),
            'character_count': len("".join(words))}

print(get_text_info("Andrew"))
print(get_text_info("Andrew is here"))

#example 2 - generate random number and check if its even

import random
def generate_number():
    # Imagine this is a more complex operation
    return random.randint(1, 100)  # Generates a random number between 1 and 100

numbers = []
for _ in range(10):  # Still wanting to check 10 numbers
    if (num := generate_number()) % 2 == 0:
        numbers.append(num)
print(*numbers)

#example 3 - read a file

#with open('file.txt', 'r') as file:
#    while (line := file.readline()):
#        print(line.strip())

#example 4

word = "test"
for char in word:
    if (upper_char := char.upper()) == char:
        print(f"{char} is uppercase.")
    else:
        print(f"{char} is not uppercase.")

word = "test"
for char in word:
    if (current_char := char.lower()) == 't':
        print(f"{char} is a 't'.")
    else:
        print(f"{char} is not a 't'.")