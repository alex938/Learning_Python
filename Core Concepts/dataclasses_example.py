import random
import string
import functools
from dataclasses import dataclass, field

def generate_random_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=10))

def fmtprice(amount, sign):
    return f"{sign}{amount}"

#kw_only requires key words in init
#slots uses slots, around 20% faster than dundar __dict__ object
#frozen class variables cant be changed
@dataclass(kw_only=True, slots=True, frozen=False)
class Game:
    title: str
    price: str
    in_stock: bool = True
    developers: list[str] = field(default_factory=list)
    #init=False (do not allow user to set ID themselves in init)
    _stock_id: str = field(init=False, default_factory=generate_random_id)
    #repr=False, removed from repr i.e. not printed
    _search_strings: str = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._search_strings = f"{self.title} {' '.join(self.developers)}"

def main() -> None:
    game1 = Game(title="Diablo 4", price=fmtprice(59.99, "£"), developers=["Blizzard", "Microsoft"])
    game2 = Game(title="Diablo 5", price=fmtprice(79.99, "£"), in_stock=False)
    print(game1)
    print(game2)

    #fmtUS = functools.partial(fmtprice, sign="$")
    #print(fmtUS(20))

if __name__ == '__main__':
    main()