# Лекция про ошибки!
#try:
#    name = int(input("Введите число"))
#except:
#   print("Введено не число!")
from typing import List

#Бесконечная функция (Можно использовать где уодно. Выход по значению) + Пример try exept конструкции
short_list = [1, 2, 3]
while True:
    value = input("Position? [q to quit]")
    if value =="q":
        break

    try:
        position = int(value)
        print(short_list[position])
    except IndexError as err:
        print("Bad index: ", position)
        #Всё ошибки! (Тоже очень полезно)
    except Exception as other:
        print("Something else broke: ", other)
import random
short_list = random.choice(short_list)
print(short_list)

#

