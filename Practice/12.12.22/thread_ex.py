from threading import Thread, current_thread, Condition, Lock
from time import sleep, monotonic


class Work(Thread):
    def __init__(self, name: str):
        super().__init__(name=name)

    def run(self):
        global cur
        print(f"Thread {current_thread()} started: {round(monotonic() - cur, 4)}")
        print(current_thread().ident)
        print(f"")
        sleep(3)
        print(f"Time {current_thread().ident} for finished: {round(monotonic() - cur, 4)}")


if __name__ == "__main__":
    threads = []
    cur = monotonic()
    for i in range(5):
        thread = Work(name=f"work {i}")
        thread.start()
        threads.append(thread)
        sleep(1)
    for th in threads:
        th.join()
