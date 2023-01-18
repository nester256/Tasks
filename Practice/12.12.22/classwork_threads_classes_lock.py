from multiprocessing import Lock
from threading import Thread, current_thread
from time import sleep, monotonic


class Worker(Thread):
    def __init__(self, name: str) -> None:
        super().__init__(name=name)
        print(f"Thread Worker creared: {current_thread()}")

    def run(self):
        global number, lock
        with lock:
            print(f"Thread Worker creared: {current_thread()}")
            print(f"Number: {number}")
            for _ in range(10):
                new = number
                sleep(0.0001)
                new += 1
                sleep(0.0001)
                number = new


if __name__ == "__main__":
    lock = Lock() # блокировка на потоки (можно сделать так с философами)
    number = 0
    for _ in range(10):
        worker_thread = Worker("12-12-22")
        worker_thread.start()
    sleep(5)
    print(f"Number with worker joined: {number}")