import time
from threading import Barrier, Thread

#the barrier is initialised with Barrier(2), meaning it requires two threads to call wait() before any of them can proceed
barrier = Barrier(2)

def wait_on_barrier(name, time_to_sleep):
    for i in range(2):
        print(name, "running")
        time.sleep(time_to_sleep)
        print(name, "is waiting on barrier")
        barrier.wait()
    print(name, "is finished")

red = Thread(target=wait_on_barrier, args=["red", 4])
blue = Thread(target=wait_on_barrier, args=["blue", 10])

red.start()
blue.start()

red.join()
blue.join()

print("Both threads have finished.")