from contextlib import contextmanager, ExitStack, redirect_stdout
from datetime import datetime
import time

@contextmanager
def timer():
    start = datetime.now()
    yield #returns to the original function, then comes back after function has finished executing
    print("Time taken {} seconds".format((datetime.now()-start).seconds))

@contextmanager
def print_green():
    print("\033[32m", end="")
    yield #returns to the original function, then comes back after function has finished executing
    print("\033[39m", end="")

@contextmanager
def print_red():
    print("\033[31m", end="")
    yield #returns to the original function, then comes back after function has finished executing
    print("\033[39m", end="")

def timer_test(time_to_sleep):
    with ExitStack() as stack:
        if time_to_sleep > 2: #prints in red if the 'if statement' is true, else green
            stack.enter_context(print_red())
        else: 
            stack.enter_context(print_green())
        stack.enter_context(timer())
        time.sleep(time_to_sleep)
        print("Work complete!")

if __name__ == '__main__':
    timer_test(3)
    timer_test(1)

#Additional functionality:
#sends output to a log_file.txt
#stack.enter_context(redirect_stdout(open('log_file.txt', 'w')))

'''
Work complete!
Time taken 3 seconds
Work complete!
Time taken 1 seconds
'''