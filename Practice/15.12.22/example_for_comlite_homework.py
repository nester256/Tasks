from threading import Lock, Thread, Barrier, active_count, local
from time import sleep, monotonic
from random import randint, randrange


# Пример программы на примере сдачи дз студентами и их друзьями которые их ждут
STUDENTS = {
    "Nazarov": 0,
    "Prihodko": 0,
    "Max": 0,
    "Filatov": 1,
    "Nesterov": 1,
    "Orehov": 1,
    "Butenko": None
}

CONSULTATION_TIME = 90
SPEED_UP = 1
HOMEWORKS = list(range(6))


# Генерирует барьеры (ждёт друзей)
def generate_barriers(students: dict):
    groups = list(set(students.values()))
    groups.remove(None)
    barriers = []
    for i in sorted(groups):
        count_st = list(students.values()).count(i)
        barriers.append(Barrier(count_st))
    return barriers


def prob(percent=50):
    # Эта функция возвращает случайное значение от 0 до 99
    return randrange(100) < percent


class Student(Thread):
    COMPLETION_TIME = (3, 6)
    FIX_TIME = (1, 5)

    def __init__(self, name: str, friends: int = None):
        super().__init__(name=name, daemon=True)
        self.name = name
        self.friends = friends
        self.patiense = randrange(CONSULTATION_TIME) / SPEED_UP

    def run(self):
        global teacher, hw_table, barriers
        hw_table.to_complete = [hw for hw in HOMEWORKS if prob(20)]
        while hw_table.to_complete:
            print("Пришёл студент {} с {}".format(self.name, hw_table.to_complete))
            with teacher:
                hw = hw_table.to_complete[0]
                sleep((randint(*Student.COMPLETION_TIME) + hw) / SPEED_UP)
                if prob(50):
                    print('Студент {} сдал дз {}'.format(self.name, hw))
                    del hw_table.to_complete[0]
                else:
                    print("Студент {} НЕ Сдал дз {}".format(self.name, hw))
            sleep(randint(*Student.FIX_TIME) / SPEED_UP)
        msg = "Студент {} уходит".format(self.name)
        if isinstance(self.friends, int):
            print("Студент {} ждёт друзей".format(self.name))
            if barriers[self.friends].wait(self.patiense):
                msg += " с друзьями"
            else:
                msg += " без друзей"
        print(msg)


if __name__ == "__main__":
    hw_table = local()
    teacher = Lock()
    barriers = generate_barriers(STUDENTS)
    for name, group in STUDENTS.items():
        # barrier = barriers[group] if isinstance(group, int) else None
        Student(name, group).start()

    start = monotonic()
    while True:
        sleep(5 / SPEED_UP)
        students_count = active_count() - 1
        print(f"На консультации осталось {students_count} студентов")
        if monotonic() - start >= CONSULTATION_TIME / SPEED_UP or students_count == 0:
            print("Консультация окончена")
            break


