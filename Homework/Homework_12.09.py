# Ввод
# Вариант 1 (без пояснения)
# user_text = input();
# print("Ваш текст: ", user_text)
# Вариант 2 (с пояснениями)
# user_text = input("Введите текст: ")
# print("Ваш текст: ", user_text)

# Работа со строками
# Вариант 1
# str_1 = "%s" % "Это строка"
# print(str_1)
# Вариант 2
# str_2 = "Hi {0}".format("user_name")
# print(str_2)
# Тот же вариант с регулярным выражением
# int_1 = 4
# complex_str = "text{0:^10d}text".format(int_1)
# print(complex_str)

# Задание 0
# a = 4
# b = 6
# a = a + b
# b = a - b
# a = a - b
# print("{0} {1}".format(a, b))

# Задание 1
# stuff = {"Пылесос" : 4,
#          "Утюг" : 3,
#          "Ноутбук" : 10,
#          "Стол" : 5}
# for key in stuff :
#     #print("Количество %sов: %d" % (key, stuff[key]))
#     print("Количество {0}ов: {1}".format(key, stuff[key]))

# Задание 2
# u_str = str (input())
# print(u_str == u_str[::-1])

# Задание 3
#     names = [i for i in user_names.split()]
#     user_len = len(names)
#     if user_len <1:
#         print("Ты никому не нужен")
#     if user_len == 1:
#         print(names[0]+ "likes it")
#     if user_len == 2:
#         print("{0} and {1} like it".format(names[0],names[1]))
#     if user_len==3:
#         print("{0} ,{1} and {2} like it".format(names[0],names[1],names[2]))
#     else :
#         users = user_len -1
#         print("{0} and {1} like it".format(names[0],users))

# Задание 4
# mini_letters = 0
# big_letters = 0
#     for letter in s:
#         if letter.islower():
#             mini_letters+=1
#         else:
#             big_letters+=1
#     str_len = len(s)
#     first_percent = mini_letters/str_len * 100
#     second_percent = big_letters/str_len * 100
#     print("Процент маленьких букв - {0} , Процент больших букв - {1}".format(first_percent,second_percent))

# ДЗ Задание 5 Посчитать % строк где больше загл букв
def find_big_letters(s):
    mini_letters = 0
    big_letters = 0
    for letter in s:
        if letter.islower():
            mini_letters += 1
        else:
            big_letters += 1
    if big_letters > mini_letters:
        return True
    else:
        return False


strings = str(input()).split()
string_len = len(strings)
big_str = 0
small_str = 0
for string in strings:
    if find_big_letters(string):
        big_str += 1
    else:
        small_str += 1

first = big_str / string_len * 100
second = small_str / string_len * 100

print("big :{0} percent, small :{1} percent".format(first, second))

# ДЗ Задание 6 (Вообще 5, но мне было интересно его сделать)
# string = str (input("Введите строку:"))
# sub_string = str (input("Введите подстроку:"))
# for i in range(len(string)):
#     h = ""
#     for j in range(len(sub_string)):
#         if i + j < len(string):
#             h += string[i + j]
#         if h == sub_string:
#             print(i)
