from threading import Thread, current_thread
from time import sleep, monotonic


def add_10():
    global number
    # print(current_thread())
    # print(current_thread().ident)
    for _ in range(10):
        new = number
        sleep(0.0001)
        new += 1
        sleep(0.0001)
        number = new


if __name__ == '__main__':
    # print(current_thread())
    # print(current_thread().ident)
    number = 0
    time_init_threads = monotonic()
    threads = []
    for i in range(100):
        thread = Thread(target=add_10, name=f"meThread{i}")
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    print('Number: {0}'.format(number))
    print("Time with treads: {}".format(monotonic() - time_init_threads))
    time_init_serial = monotonic()
    for i in range(100):
        add_10()
    print('Number: {0}'.format(number))
    print("Time with treads: {}".format(monotonic() - time_init_serial))

    # sleep(0.1)

