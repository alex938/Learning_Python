from multiprocessing import Process, set_start_method
import time
import os

def worker(function, *args):
    process = Process(target=function, args=args)
    process.start()

def print_numbers(*args):
    for number in args:
        print(f"Process ID: {os.getpid()}, Number: {number}")
        time.sleep(1)

if __name__ == '__main__':
    set_start_method('spawn')
    worker(print_numbers, 1, 2, 3, 4, 5)
    worker(print_numbers, 6, 7, 8, 9, 10)