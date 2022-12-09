# Потоки и процессы
from multiprocessing import Process, Barrier, Event
from random import randint
from time import sleep


def out_red(text):
    print("\033[31m{}\033[0m" .format(text))


def out_yellow(text):
    print("\033[33m{}\033[0m" .format(text))


def out_blue(text):
    print("\033[34m{}\033[0m" .format(text))


class Student(Process):
    TIME_OF_WAIT = 4
    X = randint(1, 3)
    Y = randint(1, 5)

    def __init__(self, name: str, classroom: Barrier, action: Event, k=1):
        super().__init__()
        self.action = action
        self.classroom = classroom
        self.name = name
        self.k = k

    def run(self):
        out_red("Студент {} приходит на экзамен".format(self.name))
        out_red("Студент {} раздевается".format(self.name))
        sleep(self.X)
        out_red("Студент {} ищет аудиторию".format(self.name))
        sleep(self.Y)
        self.classroom.wait()
        out_yellow("Студент {} заходит в аудиторию".format(self.name))
        if self.action.wait(timeout=self.TIME_OF_WAIT * self.k):
            out_blue("Студент {} начинает писать экзамен".format(self.name))
        else:
            out_blue("Студент {} недождался и ушёл".format(self.name))


STUDENTS = {"Viktor" : 4, "Maksim" : 2, "Volandemort" : 5, "Dima" : 9, "Yaroslav" : 1}

if __name__ == '__main__':
    classroom_0304 = Barrier(len(STUDENTS) + 1)
    teacher = Event()
    for student_name in STUDENTS.keys():
        Student(student_name, classroom_0304, teacher, STUDENTS[student_name]).start()
    classroom_0304.wait()
    out_red('Аудитория открылась студенты ждут преподавателя')
    sleep(7)
    teacher.set()
    print('Преподаватель приходит')
