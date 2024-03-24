number: int = 10
word: str = "A word"
floating_number: float = 10.2

def to_upper(elements: list[str]) -> list[str]:
    return [element.upper() for element in elements]

list1: list[str] = to_upper(["John", "Bret", "Jessica"])

print(list1)