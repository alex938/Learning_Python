from concurrent.futures import ProcessPoolExecutor
from os import getpid

def calc_cube(value):
    '''calculate a cube'''
    print(f'executing PID {getpid()}')
    return (value, value ** 3)

def main():
    with ProcessPoolExecutor(max_workers=4) as my_ppe:
        return list(my_ppe.map(calc_cube, range(10)))
    
if __name__ == "__main__":
    print(main())
