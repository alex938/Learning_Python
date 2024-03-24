set_1: set[int] = {10, 2, 4, 223}
set_2: set[int] = {11, 4, 223, 100, 101}

set_3: set[int] = set_1 | set_2
set_4: set[int] = set_1 - set_2
set_5: set[int] = set_2 - set_1
set_6: set[int] = set_2 & set_1 #elements that are shared
set_7: set[int] = set_1 ^ set_2 #unique elements

print(set_3)
print(set_4)
print(set_5)
print(set_6)
print(set_7)

