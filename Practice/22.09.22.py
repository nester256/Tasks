# Движение по двум элементам списка
# nums = [3, 4, 5, 6]
# for num, i in zip(nums, range(len(nums))):
#     print("Index: {0}  Value: {1}".format(i, num))

# Тернарный оператор
# b = 7
# a = 5 if b < 10 else 0
# print(a)

# Включения
# print(nums := [i for i in range(11)])

# Включения в словари
# dict_1 = {i: i ** 2 for i in range(11)}
# print(dict_1)

# Включения в словари сложнее
# keys = ["key_1", "key_2"]
# values = [0, 1]
# dict_1 = {key: val for key, val in zip(keys, values)}
# print(dict_1)

# Работа с файлами r - флаг чтения, a - флаг записи
f = open("pi", "a+")
# text = f.read()
# lines = f.readlines()
# print(text)
f.write("Генератор")
print(f.read())
f.close()
