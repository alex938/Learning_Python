def main():
    nato: list[str] = ["zero", "wun", "two", "three", "fower", "five", "six", "seven", \
            "eight", "niner", "alpha", "bravo", "charlie", "delta", "echo", \
                "fox-trot", "golf", "hotel", "india", "juliet", "kilo", "lima", \
                    "mike", "november", "oscar", "papa", "quebec", "romeo", \
                        "sierra", "tango", "uniform", "victor", "whiskey", \
                            "x-ray", "yankee", "zulu"]

    alphabet_numbers: list[str] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', \
                        '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', \
                            'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', \
                                'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    #print(len(nato), len(alphabet_numbers))

    code: dict[str, str] = dict(zip(alphabet_numbers, nato))

    #print(code)

    word: str = input("Enter word: ")

    for x in word.upper():
        print(code.get(x, "{} not found").format(x))

if __name__ == '__main__':
    main()