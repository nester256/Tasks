from multiprocessing import Process, Lock, Semaphore, Barrier
from time import sleep
from random import randint
from string import ascii_letters


def work(name: str, pc: Semaphore, shuttle: Semaphore, group: Barrier):
    print('Student {} has acquired a PC'.format(name))
    with pc:
        print('Student {} got a PC'.format(name))
        sleep(randint(1, 3))
    print('Student {} finished working on pc'.format(name))
    print('Student {} has come to the shuttle'.format(name))

    with shuttle:
        print('Student {} got inside shuttle'.format(name))
        sleep(randint(1, 3))
    print('Student {} has left shuttle'.format(name))
    group.wait()


STUDENTS = list(ascii_letters[:10])
ST_NUM = len(STUDENTS)
GROUP = 3


def wait_group(group_num: int, group: Barrier):
    group.wait()
    print("Group #{} goes home now".format(group_num))


if __name__ == '__main__':
    lock = Lock()
    groups = [Barrier(GROUP + 1) for _ in range(ST_NUM // GROUP)]
    md_group = ST_NUM % GROUP
    if md_group:
        groups.append(Barrier(md_group + 1))
    pc = Semaphore(2)
    shuttle = Semaphore(3)
    for i, name in enumerate(STUDENTS):
        group = groups[i // GROUP]
        Process(target=work, args=(name, pc, shuttle, group)).start()
    for i, group in enumerate(groups):
        Process(target=wait_group, args=(i, group)).start()
    sleep(1)  # <-- Adding this solves the issue on OSX
