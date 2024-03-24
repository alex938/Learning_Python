the_peope: list[str] = ["Johnny", "Bret", "Jessica"]

names: list[str] = [name for name in the_peope if len(name) > 4]

print(names)