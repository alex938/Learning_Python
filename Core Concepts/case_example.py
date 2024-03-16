a = 10
match a:
    case 1: print("Too low")
    case 100: print("Too high")
    case 10: print("Just right")
    case _: print("No matches")