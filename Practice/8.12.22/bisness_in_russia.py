from multiprocessing import Process, Condition, Lock
from random import randint
from time import sleep


def worker(end_work: Condition):
    print("Работник получил задачу и начал стричь ШПИЦА")
    sleep(randint(1, 3))
    print("Работник закончил стричь ШПИЦА")
    with end_work:
        end_work.notify()


if __name__ == '__main__':
    print("Начальник даёт работнику задание подстричь ШПИЦА!")
    end_of_work = Condition(lock=Lock())
    Process(target=worker, args=(end_of_work, )).start()
    print("Начальник пьёт чай")
    with end_of_work:
        end_of_work.wait()
    print("Начальник уходит")
    sleep(1)
