# Процеесами
from time import monotonic, sleep
from multiprocessing import Process

COUNTER = 1000

def print_many(n):
    for j in range(COUNTER):
        print("Print_many #{0}: iteration#{1}".format(n,j))


procs = []
initial = monotonic()
if __name__ == '__main__':
    for i in range(4):
        pr = Process(target=print_many, args=(i,))
        pr.start()
        procs.append(pr)

    for pr in procs:
        pr.join()

    print("Time: ", monotonic() - initial)