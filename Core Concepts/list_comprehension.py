the_people: list[str] = ["Johnny", "Bret", "Jessica"]

names: list[str] = [name for name in the_people if len(name) > 4]

print(names)