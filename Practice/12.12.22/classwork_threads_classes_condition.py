from threading import Thread, current_thread, Condition, Lock
from time import sleep, monotonic

# Этот пример тоже можно использовать для философов

class Worker(Thread):
    def __init__(self, name: str) -> None:
        super().__init__(name=name)
        print(f"Thread Worker creared: {current_thread()}")

    def run(self):
        global notifier
        with notifier:
            print(f"Thread Worker started: {current_thread()}")
            sleep(2)
            print(f"Thread Worker finished: {current_thread()}")
            notifier.notify()


class Boss(Thread):
    def __init__(self, name: str="Boss"):
        super().__init__(name=name)
        print(f"Boss created: {current_thread()}")

    def run(self):
        global notifier
        with notifier:
            notifier.wait()
            print(f"The boss sees that the work is done")


if __name__ == "__main__":
    notifier = Condition(lock=Lock())
    Boss().start()

    Worker('Ivan').start()
