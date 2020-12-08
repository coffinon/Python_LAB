import threading
import random
import time


class Philosopher(threading.Thread):
    running = True

    def __init__(self, name, left_fork, right_fork):
        threading.Thread.__init__(self)
        self.name = name
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        while self.running:
            time.sleep(random.random())
            print(self.name, " chce jesc ...")
            self.dine()

    def dine(self):
        while self.running:
            self.left_fork.acquire(True)
            locked = self.right_fork.acquire(False)
            if locked:
                break
            self.left_fork.release()
            print(self.name, " zamienia widelce ...")
            self.left_fork, self.right_fork = self.right_fork, self.left_fork
        else:
            return

        self.dining()
        self.right_fork.release()
        self.left_fork.release()

    def dining(self):
        print(self.name, " zaczyna jesc ...")
        time.sleep(random.random() * 5)
        print(self.name, " konczy jesc i odklada widelce ...")


forks = []
philosophers = []

for i in range(0, 5):
    forks.append(threading.Lock())

for i in range(0, 5):
    philosophers.append(Philosopher("Filozof " + str(i), forks[i % 5], forks[(i + 1) % 5]))

Philosopher.running = True
random.seed()

for i in range(0, 5):
    philosophers[i].start()

time.sleep(30)
Philosopher.running = False
print("Filozofowie koncza uczte ...")
