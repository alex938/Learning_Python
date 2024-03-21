import time
from threading import Thread

threads = []

def work():
    print("Starting work")
    i = 0
    for _ in range(20000000):
        i += 1
    print("Finished work")

for _ in range(5):
    t = Thread(target=work)
    t.start()
    threads.append(t)

for t in threads:
    t.join() 