def concat_phone_number(*, network: str, number: str) -> str:
    return network + number

def main() -> None:
    network: str = "27567"
    number: str = "844488"

    print(concat_phone_number(network=network, number=number))

if __name__ == '__main__':
    main()

'''
def func1(x, y):
    c = x + y
    return c

def main():
    num1 = "27567"
    num2 = "844488"

    print(func1(num1, num2))

if __name__ == '__main__':
    main()
'''
