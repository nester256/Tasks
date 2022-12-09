def valid_phone(number):
    len_num = len(number) == 16
    start = number[:3] + number[6] == "+7()"
    then = (number[3:6] + number[7:10] + number[11:13] + number[14:]).isdigit()
    end = number[10] + number[13] == "--"
    return start and then and end and len_num
