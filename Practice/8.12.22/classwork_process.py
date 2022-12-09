# Прочстой тест кондишона на процессы (запускаются один за одним и работают паралельно)
from datetime import datetime
from multiprocessing import Process, Condition, Lock
from os import getpid
from time import sleep


def work(cond: Condition):
    with cond:
        cond.wait()
    for i in range(5):
        time = datetime.now().isoformat()[-15:]
        print("Process {} iteration #{} at {}".format(getpid(), i, time))
        sleep(1)


PROCESS = 3

if __name__ == "__main__":
    cond = Condition(lock=Lock())
    for _ in range(PROCESS):
        Process(target=work, args=(cond, )).start()
    for _ in range(PROCESS+1):
        with cond:
            cond.notify()
        sleep(1)
