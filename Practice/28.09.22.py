# функция проверяет существование файла и файл ли это
# Если его нет - создаёт
import os
import shutil


def check_valid_file(file_name):
    isExist = os.path.exists(file_name)
    isFile = os.path.isfile(file_name)
    if isExist and isFile:
        print("Всё отлично!")
    else:
        new_file = open(file_name, "w")
        new_file.close()
        print("Всё отлично! Файл создан!")


# check_valid_file("123")

# 12.02.2022
from datetime import date, timedelta


def some_date(cur_date, n):
    """
    This function does something
    :param cur_date: format date(dd.mm.yyyy)
    :param n: decimal number
    :return: datetime date in ISO format
    """
    try:
        my_date = [int(i) for i in cur_date.split(".")]
    except Exception as e:
        print("Ошибка! ", e)
    else:
        cur_date = date(my_date[2], my_date[1], my_date[0])
        interval = timedelta(days=n)
        return (cur_date + interval).isoformat()


# print(not some_date("12.Привет.2022", 100) is None)

def del_file(my_path, string):
    for path, _, files in os.walk(my_path):  # Тут циганские фокусы
        for file in files:
            if string in file:
                # os.remove(os.path.join(path, file))
                os.system("rm \"{0}\"".format(os.path.join(path, file)))


def move_file(file_path, new_path):
    if os.path.exists(file_path) and os.path.isfile(file_path):
        if os.path.exists(new_path) and os.path.isdir(new_path):
            shutil.move(file_path, new_path)
        else:
            print("dir for move is`t exist")
    else:
        print("file is`t exist")
