# It`s my homework
# Функция лога капитана, на вход даётся список строк (записей), и дата начала.
# Функция создаёт файл лога
from datetime import datetime, timedelta


def insanity_captain(list_of_insanity_notes: list, date_of_start: str):
    """
    This function accepts a list of the captain's records and the start date of the records.
    Args:
        list_of_insanity_notes: list of strings notes
        date_of_start: string of start date
    """
    try:
        my_date = datetime.strptime(date_of_start, '%d-%m-%Y')
    except Exception as e:
        print("Ошибка!", e)
    else:
        log_file = open("log_of_insanity_captain.txt", "w")
        for i in range(len(list_of_insanity_notes)):
            log_file.writelines(str((my_date + timedelta(days=i)).strftime('%d-%m-%Y')) + " : " + \
                                list_of_insanity_notes[i] + "\n")
        log_file.close()

# insanity_captain(["Плывём", "Не плывём", "Тонем"], "20-02-1678")
