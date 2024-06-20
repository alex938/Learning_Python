from concurrent.futures import ThreadPoolExecutor
import threading

def calc_cube(value):
    '''calculate a cube'''
    print(f'executing {threading.current_thread().name}')
    return (value, value ** 3)

my_tpe = ThreadPoolExecutor(max_workers=3)
results = my_tpe.map(calc_cube, range(10))
print(list(results))
