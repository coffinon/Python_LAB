import threading
import random
import time

histogram_parts = [0, 0, 0, 0, 0]
exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name, data):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.data = data

    def run(self):
        print("Starting " + self.name)
        print_time(self.name, self.data, 0.1)
        print("Exiting " + self.name)


def print_time(threadName, data, delay):
    for i in range(0, len(data)):
        if exitFlag:
            threadName.exit()
        time.sleep(delay)

        if data[i] < 20:
            histogram_parts[0] += 1
            print(threadName, "element assigned to 1st part\n")
        elif data[i] < 40:
            histogram_parts[1] += 1
            print(threadName, "element assigned to 2nd part\n")
        elif data[i] < 60:
            histogram_parts[2] += 1
            print(threadName, "element assigned to 3rd part\n")
        elif data[i] < 80:
            histogram_parts[3] += 1
            print(threadName, "element assigned to 4th part\n")
        else:
            histogram_parts[4] += 1
            print(threadName, "element assigned to 5th part\n")


random.seed()
data = []

for i in range(0, 100):
    data.append(int(random.random() * 100))

thread1 = myThread(1, "Thread-1", data[:50])
thread2 = myThread(2, "Thread-2", data[50:])

thread1.start()
thread2.start()

while 1:
    if sum(histogram_parts) == 100:
        time.sleep(1)
        print("_-_-_-_-_ HISTOGRAM _-_-_-_-_")
        print(" 1 - 20  : ", histogram_parts[0] * "*")
        print("21 - 40  : ", histogram_parts[1] * "*")
        print("41 - 60  : ", histogram_parts[2] * "*")
        print("61 - 80  : ", histogram_parts[3] * "*")
        print("81 - 100 : ", histogram_parts[4] * "*")
        break
