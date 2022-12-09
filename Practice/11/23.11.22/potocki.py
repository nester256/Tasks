# Потоки
from time import monotonic, sleep
from threading import Thread
COUNTER = 10

def print_many(n):
    for j in range(COUNTER):
        print("Print_many #{0}: iteration#{1}".format(n,j))
        sleep(0.2)

threads = []
initial = monotonic()
if __name__ == '__main__':
    for i in range(4):
        thread = Thread(target=print_many, args=(i,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print("Time: ", monotonic() - initial)