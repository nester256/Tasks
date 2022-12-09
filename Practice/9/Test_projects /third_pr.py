def find_substring(string, sub):
    sub_l = len(sub)
    for i in range(len(string) - sub_l):
        if string[i:i + sub_l] == sub:
            return i
    return -1


# print(find_substring("abcdefg", "ef"))

def print_dict_for_tree_methods(dict_1, method):
    for key in dict_1.keys():
        if method == 0:
            print("{0} {1}".format(key, dict_1[key]))
        elif method == 1:
            print("%s  %d" % (key, dict_1[key]))
        elif method == 2:
            print(f"{key} {dict_1[key]}")
        else:
            print("Такого метода не существует!")
            return


dict_2 = {"Пылесос": 4,
          "Утюг": 3,
          "Ноутбук": 10,
          "Стол": 5}


# print_dict_for_tree_methods(dict_2, 2)

def refresh_list(list_1):
    for i in range(len(list_1)):
        v1 = list_1[i].split(" ")
        list_1[i] = v1[0][0] + " " + v1[1]
    return list_1


print(refresh_list(["Владислав Нестеров", "Денис Нечитайло"]))


def gen(first, last, step):
    num = first
    res = []
    while first < last:
        res.append(num)
        num += step
    return res
