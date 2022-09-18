"""
list_1 = [1, 2]
list_1.append(1)
list_1.insert(0, 2)
list_1 += [4]
list_1.extend([5, 6])
list_1.pop(0)
list_1.remove(5)
print(list_1)
"""
# empty_dict = dict()
# print(empty_dict)
# print(type(empty_dict))
# empty_dict["key"] = "value"
# print(empty_dict)
# empty_dict["key"] = ["value_2", empty_dict["key"]]
# print(empty_dict["key_3"])

#tuple_1 = (1, 2, 3)

# set_1 = {1, 2, 3, 4}
# set_2 = {3, 4, 5, 6}
# set_1.add(0)
# print(set_1.intersection(set_2))
# print(set_1 & set_2)

# a = 6
# if a < 5 :
#     print("!")
# elif a > 5: 
#     print("?")

# a = 0
# while a < 5:
#     print(a)
#     a += 1
#     if a == 2:
#         print("Мы дошли до двойки!")
#         continue

# list_1 = []
# i = 1
# while len(list_1) < 10: 
#     list_1.append(i)
#     i += 1

# for i in list_1:
#     print(i)

# for i in range(10, 0, -2):
#     print(i)

list_1 = ["Влад", "Диана", "Катя", "Ника"]  #Объявляем имена
names_dict = dict()                         #Объявяем словарь
i = 0                                       #Объявялем вспомогатльную переменную
for name in list_1:                         #Цикл по именам
    names_dict[i] = list_1[i]               #Присваиваем к каждому ключу значение
    i += 1                                  #Увеличиваем i на 1
print(names_dict)                           #После выполнения цикла выводим наш готовый словарь

