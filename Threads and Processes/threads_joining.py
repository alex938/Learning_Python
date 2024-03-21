import threading
import time

def child():
    print("Child thread started...")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("5")
    time.sleep(1)
    print("Child thread finished.")

def parent():
    t = threading.Thread(target=child, args=())
    t.start()
    print("Parent waiting...")
    #waits at this join point for child to finish
    t.join()
    print("Parent unblocked.")

parent()