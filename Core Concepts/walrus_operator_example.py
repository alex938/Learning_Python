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