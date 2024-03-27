from threading import Thread
import time as t

def worker(function, *args):
    thread = Thread(target=function, args=args)
    print(thread.name)
    thread.start()

def print_numbers(*args):
    for number in args:
        print(number)
        t.sleep(1)

worker(print_numbers, 1, 2, 3, 4, 5) 
worker(print_numbers, 1, 2, 3, 4, 5)