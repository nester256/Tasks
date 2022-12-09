# Простыми функциями
from time import monotonic, sleep

COUNTER = 20

def print_many(n):
    for j in range(COUNTER):
        print("Print_many #{0}: iteration#{1}".format(n,j))
        sleep(0.1)

initial = monotonic()
for i in range(4):
    print_many(1)

print("Time: ", monotonic() - initial)