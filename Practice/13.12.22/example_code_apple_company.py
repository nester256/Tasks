from random import choice, randint, uniform
from threading import Event, Thread, current_thread, local
from time import monotonic, sleep


class IPhone:
    MODELS = ["SE", "S", "XS", "X", "PRO", "PRO MAX", "EXTRA"]
    VERSION = 1
    NEWEST_K = 1

    def __init__(self) -> None:
        model = choice(IPhone.MODELS)
        self.name = f"iPhOnE {IPhone.VERSION} {model}"
        self.price = 99000 + IPhone.MODELS.index(model) * IPhone.NEWEST_K * 10000
        IPhone.VERSION += 1
        IPhone.NEWEST_K *= 1.1


class Cumstomer(Thread):
    def __init__(self, name: str, money: float, salary: float, pride_day: Event):
        super().__init__()
        self.name = name
        self.money = money
        self.float = float
        self.salary = salary
        self.pride_day = pride_day

    def run(self):
        global iphone, initial
        while True:
            self.pride_day.wait()
            money_earned = round(self.salary * (monotonic() - initial), 2)
            print(f"Customer {self.name} have earned {money_earned}")
            self.salary += money_earned
            if self.money >= iphone.price:
                print(f"Customer {self.name} succesfully bought {iphone.name}")
                self.money -= iphone.price
            else:
                print(f"---Customer {self.name} are sent into Podolsk!---")
                break


INTERVAL = (2, 4)
MONEY_INTERVAL = 150000.0, 1000000.0
SALARY_INTERVAL = 15000.0, 35000.0

if __name__ == "__main__":
    initial = monotonic()
    iphone = None
    pride_day = Event()
    for i in range(4):
        Cumstomer(str(i), uniform(*MONEY_INTERVAL), uniform(*SALARY_INTERVAL), pride_day).start()
    while True:
        iphone = IPhone()
        print(f"NEW BOY IN THIS GYM: {iphone.name} is {round(iphone.price, 2)}")
        pride_day.set()
        pride_day.clear()
        sleep(randint(*INTERVAL))