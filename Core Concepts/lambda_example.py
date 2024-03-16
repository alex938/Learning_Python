c = [["frank", 18],["phil", 7],["jess", 10]]

print(c)

d = sorted(c, key=lambda x: x[1])

print(d)

d = sorted(c, key=lambda x: x[1], reverse=True)

print(d)