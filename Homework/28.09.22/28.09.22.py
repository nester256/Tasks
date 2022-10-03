# It`s my homework
# Функция лога капитана, на вход даётся список строк (записей), и дата начала.
# Функция создаёт файл лога
# from datetime import date, timedelta


# def insanity_captain(list_of_insanity_notes, date_of_start):
#     try:
#         my_date = [int(i) for i in date_of_start.split(".")]
#     except Exception as e:
#         print("Ошибка!", e)
#     else:
#         cur_date = date(my_date[2], my_date[1], my_date[0])
#         log_file = open("log_of_insanity_captain.txt", "w")
#         for note in list_of_insanity_notes:
