def valid_d(date):
    """
        This function is required for date validity
        :arg
            date: string (Required to enter the value to be checked)
        :return:
            boolean - If this date exists
        """

    def is_leap_year(year_str):
        """
        This function checks if the year is leap year
        :arg
            year_str:
        :return:
            boolean - If year is leaped
        """
        year = int(year_str)
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    date_str = date.split(".")

    # print("Число:", date_str[0], "Месяц:", date_str[1], "Год:", date_str[2])
    try:
        month = int(date_str[1])
        day = int(date_str[0])
    except Exception:
        print("Ошибка! Неверный формат!")
        return False
    if 1 <= month <= 12:
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            return True if (1 <= day <= 31) else False
        elif month == 4 or month == 6 or month == 9 or month == 11:
            return True if (1 <= day <= 30) else False
        elif month == 2:
            if is_leap_year(date_str[2]):
                return True if (1 <= day <= 29) else False
            else:
                return True if (1 <= day <= 28) else False
    else:
        return False
