from typing import List


def find_char_in_line(char: str, line: str) -> List[int]:
    """
    Эта функция ищет вхождения символа
    :param char: искомый символ
    :param line: исходная строка
    :return:
    Возвращает список индексов сторки
    """
    list_of_indexes = []
    try:
        if len(char) <= 1:
            for i in range(len(line)):
                if line[i] == char:
                    list_of_indexes.append(i)
            if len(list_of_indexes) == 0:
                print("Ничего не найдено")
            print(list_of_indexes)
        else:
            print("Количество символов не соответствует условию!")
    except TypeError:
        print("Введён не текст!")
    except Exception as er:
        print("Другая ошибка {0}".format(er))


print("Первый запуск")
find_char_in_line("b", "abbaka")
print("\nВторой запуск")
find_char_in_line("a", "abbaka")
print("\nТретий запуск")
find_char_in_line("a", 123)
print("\nЧетвёртый запуск")
find_char_in_line("a", "123")
