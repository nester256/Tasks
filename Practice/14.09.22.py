# 14.09.22
# Рандомное заполнение
# import random
# nums = [random.randint(0, 10) for _ in range(10)]
# print(nums)

# Сортировка первым методом (который изменяет сразу объект)
# nums = [9, 6, 4, 7, 1, 10, 6, 6, 4, 7]
# nums.sort(reverse=True)
# print(nums)

# Сортировка вторым методом (который не изменяет объекты)
# new_nums = sorted(nums)
# print(new_nums)

# Сортировка через лябда функцию по 2 элементу
# results = [("X", 8), ("Y", 10), ("Z", 7)]
# results.sort(key=lambda x:x[1], reverse=False)
# print(results)

# Функция фильтра
# def is_even(el):
#     return el % 2 == 0
# nums = [9, 6, 4, 7, 1, 10, 6, 6, 4, 7]
# for i in filter(lambda el : el % 2 == 0, nums):
#     print(i)
# print(nums)

# def cube(x):
#     return x ** 3

# Работа с мап, он применяет функцию к каждому элементу
# nums = [0, 1, 2, 3]
# new_nums = list(map(lambda el : el ** 3, nums))
# print(new_nums)

# Генераторы в 2
# def first_task(n, m):
#     if m == 0:
#         i = 1
#         while i < n:
#             yield i
#             i += 2
#     if m == 1:
#         for i in range(n):
#             yield i if not(i % 2 == 0) else ""
# for i in first_task(9, 1):
#     print(i, end = " ")

def second_task(text):
    words = text.split()
    new_words = list(map(lambda x: x.capitalize(), words))
    return " ".join(new_words)


print(second_task("привет сосед как твои дела"))
