a = 10
if isinstance(a, int): 
    b = lambda x: print(a ** 2)
    b(a)
else: print("False")