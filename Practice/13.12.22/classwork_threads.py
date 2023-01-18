from threading import Timer
from os import _exit
from time import sleep


def finish():
    print('Сработал таймер')
    _exit(0)  #код 0, что все хорошо завершилось


DATA = {"username": "qwerty"}


if __name__ == '__main__':
    login = input("Введите логин: ")
    timer = Timer(7., finish)
    for login in DATA.keys():
        timer.start()
        password = input("Введите пароль: ")
        if DATA[login] == password:
            msg = "Авторизация успешна"
        else:
            msg = "ошибка"
        print(msg)