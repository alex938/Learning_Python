def main():
    total: list = []

    for x in range(1, 1000):
        if (x % 3 == 0 or x % 5 == 0): total.append(x)

    print("Numbers: {}".format("".join(str(total))))
    print("\nTotal is: {}".format(sum(total)))

if __name__ == '__main__':
    main()