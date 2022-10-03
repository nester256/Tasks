import os


# Вывод всего файла
# file = open("file", "r")
# print(file.read())
# file.close()

# #Вывод по строкам
# file = open("file.txt", "r")
# for line in file.readlines():
#     print(line)
# file.close()

# #Добавление текста
# file = open("file.txt", "a")
# lines = ["10 11 12", "13 14 15"]
# file.writelines(["\n" + line for line in lines])
# file.close()

def function_1(file_name, n):
    try:
        print("Файл есть!" if os.path.exists(file_name) else "Файла нет :(")
        file = open(file_name, "w")
    except FileNotFoundError:
        print("Неверное название файла!")
    except Exception as err:
        print("Возникла ошибка!", err)
    else:
        file.writelines([str(num) + "\n" for num in range(1, n + 1)])
        file.close()


# function_1("file.text", 10)

def function_2(file_name, num_pow):
    try:
        # print("Файл есть!" if os.path.exists(file_name) else "Файла нет :(")
        file = open(file_name, "r")
    except FileNotFoundError:
        print("Неверное название файла!")
    except Exception as err:
        print("Возникла ошибка!", err)
    else:
        try:
            pow_numbers = (int(num) ** num_pow for num in file.readlines())
            file.close()
        except Exception as err:
            print("Возикла ошибка при чтении файла", err)
        else:
            new_file = open("new_file.txt", "w")
            new_file.writelines([str(num) + "\n" for num in pow_numbers])
            new_file.close()


function_2("file.txt", 2)

# def function_3(conf_file_name):
#     conf_file = open(conf_file_name, "r")
#     dict_conf = {}
