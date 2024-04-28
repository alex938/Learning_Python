import tracemalloc

def concat_phone_number(*, network: str, number: str) -> str:
    return network + number

def main():
    tracemalloc.start() 

    network = "27567"
    number = "844488"

    for _ in range(100):
        concat_phone_number(network=network, number=number)

    current, peak = tracemalloc.get_traced_memory()
    print("Current memory usage: {} bytes\nPeak memory usage: {} bytes".format(current, peak))

    tracemalloc.stop()  

if __name__ == '__main__':
    main()

