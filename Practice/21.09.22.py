def f_1(string, char):
    return string.replace(char, "")


# print(f_1("Привет!", "!"))

def f_2(dict_1, list_1):
    new_list = []
    for key in dict_1.keys():
        for n_kay in list_1:
            if n_kay == key and new_list.count(dict_1[key]) < 1:
                new_list.append(dict_1[key])
    return new_list


dict_2 = {"Пылесос": 4,
          "Утюг": 3,
          "Ноутбук": 10,
          "Стол": 10}
# print(f_2(dict_2,["Пылесос", "Ноутбук", "Стол"]))

import string


def f_3(n=26, step=1):
    if 1 <= n <= 26 and step >= 1:
        abc = string.ascii_lowercase
        for i in range(0, n, step):
            print(abc[i])
    else:
        print("Неверно введены аргументы")


f_3(10, 2)


def f_4():
    try:
        num = int(input("Введите число: "))
        m = int(input("Введите степень: "))
    except ValueError:
        print("Введено не число!")
    except Exception as err:
        print("Возникла ошибка!", err)
    else:
        print(num ** m)


# f_4()

def f_5(list_5, list_6):
    new_list = []
    for str_1 in list_5:
        for str_2 in list_6:
            if str_2 == str_1:
                new_list.append(str_1)
    return new_list


#print(f_5([1, 2, 3, 4], [3, 4, 5, 6]))
#   sets