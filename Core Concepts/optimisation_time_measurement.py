import timeit
import dis

def concat_phone_number(*, network: str, number: str) -> str:
    return network + number

def func1(x, y):
    c = x + y
    return c

def main():
    network: str = "27567"
    number: str = "844488"

    print("Output from concat_phone_number: {}".format(
        concat_phone_number(network=network, number=number)))

    setup_code = '''
from __main__ import concat_phone_number
network = '27567'
number = '844488'
'''

    function_time = timeit.timeit(
        'concat_phone_number(network=network, number=number)',
        setup=setup_code,
        number=200000
    )
    print("Time for concat_phone_number: {:.2f} milliseconds".format(
        function_time * 1000))

    num1 = "27567"
    num2 = "844488"

    print("Output from func1: {}".format(
        func1(num1, num2)))

    setup_code = '''
from __main__ import func1
num1 = '27567'
num2 = '844488'
'''

    function_time = timeit.timeit(
        'func1(num1, num2)',
        setup=setup_code,
        number=200000
    )
    print("Time for func1: {:.2f} milliseconds".format(
        function_time * 1000))
    
    print("Disassembly of concat_phone_number:")
    dis.dis(concat_phone_number)

    print("\nDisassembly of func1:")
    dis.dis(func1)

if __name__ == '__main__':
    main()

'''
Output from concat_phone_number: 27567844488
Time for concat_phone_number: 16.30 milliseconds
Output from func1: 27567844488
Time for func1: 17.53 milliseconds
Disassembly of concat_phone_number:
  5           0 LOAD_FAST                0 (network)
              2 LOAD_FAST                1 (number)
              4 BINARY_ADD
              6 RETURN_VALUE

Disassembly of func1:
  8           0 LOAD_FAST                0 (x)
              2 LOAD_FAST                1 (y)
              4 BINARY_ADD
              6 STORE_FAST               2 (c)

  9           8 LOAD_FAST                2 (c)
             10 RETURN_VALUE
'''