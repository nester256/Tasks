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
                return False
            return True
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
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 1 <= day <= 31
        elif month in [4, 6, 9, 11]:
            return 1 <= day <= 30
        elif month == 2:
            if is_leap_year(date_str[2]):
                return 1 <= day <= 29
            return 1 <= day <= 28
    else:
        return False
