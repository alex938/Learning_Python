import time
from threading import Thread, Lock, Condition

class sp:
    def __init__(self, money, running):
        self.money = money
        self.running = running
        self.cv = Condition()

    def save(self):
        for _ in range(100):
            self.cv.acquire()
            self.money += 10
            self.cv.notify() #notifies any waiting threads i.e. cv.wait()
            self.cv.release()

    def spend(self):
        for _ in range(200):
            self.cv.acquire()
            if self.money < 20:
                self.cv.wait() #status updated by cv.notify()
            self.money -= 20
            self.cv.release()

            if self.money <= 0 and self.running:
                self.running = False
                break

finances = sp(100, True)
print("Current money: {}".format(finances.money))

Thread(target=finances.save, args=()).start()
Thread(target=finances.spend, args=()).start()
time.sleep(5)

print("Current money: {}".format(finances.money))