from typing import Callable

a = 10
if isinstance(a, int): 
    #returns None
    #called by int or float
    b: Callable[[int | float ], None] = lambda x: print(a ** 2)
    b(a)
else: print("False")