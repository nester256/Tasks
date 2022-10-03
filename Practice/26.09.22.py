# Рекурсивные функции
def print_to_n(n):
    print(n)
    if n > 0:
        print_to_n(n - 1)


# print_to_n(5)


def print_to_nn(n):
    while n >= 0:
        print(n)
        n -= 1


# print_to_nn(5)

# Примеры рекурсивных вариантов и не рекурсивных

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# print(factorial(5))


def factoriall(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result


# print(factoriall(5))

def print_digits(n):
    print(n % 10)
    if n > 9:
        print_digits(n // 10)


# print_digits(12345)


def print_digitsss(n):
    while n > 0:
        print(n % 10)
        n = n // 10


# print_digitsss(12345)


def digits_for_right(n):
    n = str(n)
    print(int(n[0]))
    if len(n) > 1:
        digits_for_right(n[1:])


# digits_for_right(12345)

def digits_for_rightt(n):
    n = str(n)
    for sum in n:
        print(int(sum))


# digits_for_right(12345)

def sum_n(n):
    if n <= 1:
        return n
    else:
        return n + sum_n(n - 1)


# print(sum_n(6))


def sum_nn(n, sum_all=0):
    sum_all = sum_all + n
    if n <= 1:
        return n
    else:
        return n + sum_nn(n - 1, sum_all)


# print(sum_nn(6))

def sum_nnn(n):
    sum_all = 0
    while n >= 1:
        sum_all += n
        n -= 1
    return sum_all


def dels_num(m):
    for i in range(1, m + 1):
        if m % i == 0:
            yield i


# print(*dels_num(50))

def f(n):
    if n == 0:
        return 1
    else:
        return n - m(f(n - 1))


def m(n):
    if n == 0:
        return 0
    else:
        return
