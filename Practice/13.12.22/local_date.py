from random import choice
from threading import local, current_thread, Thread
from time import sleep


def thread_fun():
    id = current_thread().ident
    global data
    data.x = 0
    while True:
        print("Thread {} sees data.x={}".format(id, data.x))
        to_add = choice([0] * 4 + [1])
        if to_add:
            print("Thread {} has added 1 to data.x".format(id))
            data.x += 1
        sleep(1)


if __name__ == "__main__":
    data = local()
    for _ in range(3):
        Thread(target=thread_fun).start()
