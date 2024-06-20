import random
import time
from threading import *

# +1 due to the main thread also being included
# each row is going to be computed by 1 thread
# without work_complete, the threads will overwrite the memory space of the resulting matrix
work_start = Barrier(2)

def f():
    print("f1 start")
    work_start.wait()
    print("f1 end")

def f2():
    print("f2 start")
    work_start.wait()
    print("f2 end")

# Create Thread objects for each function
t1 = Thread(target=f)
t2 = Thread(target=f2)

# Start the threads
t1.start()
t2.start()
t1.join()
t2.join()

# Wait for the threads to complete
print("start")