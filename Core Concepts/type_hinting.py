number: int = 10
word: str = "A word"
floating_number: float = 10.2

user_name: str = "Ada"
is_valid: bool = False
average_time: float = 12.5



def to_upper(elements: list[str]) -> list[str]:
    return [element.upper() for element in elements]

list1: list[str] = to_upper(["John", "Bret", "Jessica"])



from typing import List, Tuple, Dict
user_names: List[str] = ["Ada", "Charles", "Alan"]
results: Tuple[bool] = True, False, True
config: Dict[str, int] = {"max": 100, "min": 1


                        
def myfunc1():
    """myfunc1 has no parameters
    and prints 'Hello'."""
    print("Hello")

print(help(myfunc1))

Output:
    Help on function myfunc1 in module __main__:
    
    myfunc1()
        myfunc1 has no parameters
        and prints 'Hello'.
