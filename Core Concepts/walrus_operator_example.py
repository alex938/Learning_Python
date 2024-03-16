cats = ["Frank", "Jess", "Phil"]

newlist = [(i, len(i)) for i in cats if len(i) > 4]

print(newlist)

newlist = [(i, ln) for i in cats if (ln:=len(i)) > 4]

print(newlist)