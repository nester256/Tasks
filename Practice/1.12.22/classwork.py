from multiprocessing import Process, Lock, Semaphore
import time
from random import randint
from string import ascii_letters


def work(name: str, pc: Semaphore, shuttle: Semaphore):
    print('Student {} has acquired a PC'.format(name))
    with pc:
        print('Student {} got a PC'.format(name))
        time.sleep(randint(1, 3))
    print('Stident {} finished working on pc'.format(name))
    print('Stident {} has come to the sahuttle'.format(name))

    with shuttle:
        print('Student {} got inside shuttle'.format(name))
        time.sleep(randint(1, 3))
    print('Stident {} has left shuttle'.format(name))


STUDENTS = list(ascii_letters[:10])


if __name__ == '__main__':
    lock = Lock()
    pc = Semaphore(2)
    shuttle = Semaphore(3)
    for name in STUDENTS:
        Process(target=work, args=(name, pc, shuttle)).start()
    time.sleep(1)  # <-- Adding this solves the issue on OSX
