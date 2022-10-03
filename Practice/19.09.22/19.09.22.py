# Декораторы
# **args - позиционные аргументы
# **kwargs - ключевые аргументы
import math
import time


# def announnce(function):
#     def new_f(*args, **kwargs):
#         print("Функция %s начинает работу" % function.__name__)
#         result = function(*args, **kwargs)
#         print("Функция %s закончила свою работу" % function.__name__)
#         return result
#
#     return new_f

# Второй способ
# @announnce
# def sum_two(a, b):
#     return a + b
# print(sum_two(4, 5))

# Первый способ
# new_sum = announnce(sum_two)
# print((new_sum(2, 3)))


# def show(function):
#     def new_f(*args, **kwargs):
#         print("Позиционные аргументы: ", args)
#         print("Ключевые аргументы: ", kwargs)
#         print("Имя функции: ", function.__name__)
#         result = function(*args, **kwargs)
#         return result

# return new_f


# Ещё пример
# @announnce
# @show
# def mult_string(string, mult=2):
#     return string * mult


# print(mult_string("abc"))

# И ещё примеры


# Примеры кончились, дальше идут задания
# Задание 1 (Необходимо написать свою функцию округления без использования round()
def rounding_1(num):
    print(int(num + 0.5))


# rounding_1(3.4)


# 1.1 (то же задание один только другим способом
def rounding_2(n):
    dif = n - int(n)
    if dif >= 0.5:
        return math.ceil(n)
    else:
        return math.floor(n)


# 2 функция проверки номера телефона

# print(valid_phone(input("Введите номер: ")))

# Декоратор, выводящий время выполнения функции


def time_1(function):
    def new_time(*args, **kwargs):
        print("remember time")
        inital_time = time.time()
        result = function(*args, **kwargs)
        time_gone = time.time() - inital_time
        print("time of work", time_gone)
        return result

    return new_time


@time_1
def f():
    time.sleep(3)


print(f())
