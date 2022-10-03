# Приколюхи c try except
import random
import time


def err_test_0():
    while True:
        try:
            ans = input("Введите число: ")
            if ans == "q":
                break
            print("Квадрат числа: ", int(ans) ** 2)
        except Exception as error:
            print("Возникла ошибка", error)


# err_test_0()

def err_test_1():
    while True:
        ans = input("Введите число: ")
        if ans == "q":
            break
        try:
            num = int(float(ans))
        except ValueError:
            print("Only nums!")
        except KeyboardInterrupt:
            print("Досвидания!")
        else:
            print("Квадрат вашего числа равен: ", num ** 2)
        finally:
            print("finally")


# err_test_1()


# Пример подсчёта времени
# def complex_function():
#     time.sleep(5)
#
#
# print("Засекаем время")
# initial_time = time.time()
# complex_function()
# print("Время выполнения: ", time.time() - initial_time)


def range_multiply(n, step, i=1):
    while i <= n:
        yield i
        i *= step


def time_for_method():
    for i in [1, 7]:
        start = time.time()
        quant = 10 ** i
        sorted([random.randint(0, i) for _ in range(i)])
        time.time() - start
        print("Заняло времени: %f: %f" % (quant, time.time() - start))


# time_for_method()

def change_char(ch, n):
    alph_len = 26
    n = n % 26
    num = ord(ch)
    if 65 <= num <= 91:
        start = 65
    else:
        start = 97
        num += n
        end = start + alph_len
        if num > end:
            num = start + (num - end)
        return chr(num)

    def caesar(text, n):
        result = ""
        for ch in text:
            result += change_char(ch, n)
