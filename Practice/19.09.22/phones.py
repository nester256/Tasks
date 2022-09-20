import re


def phone_validation(phone_num):
    num = phone_num[3:6] + phone_num[7:10] + phone_num[11:13] + phone_num[14:]
    length = len(phone_num) == 16
    start = phone_num[0:3] == '+7('
    middle_1 = phone_num[6] == ')'
    middle_2 = phone_num[10] + phone_num[13] == '--'
    return num.isdigit() and start and length and middle_1 and middle_2

def phone_g(num):
    return 'True' if re.fullmatch('^\\+[0-9]{1}\\([0-9]{3}\\)[0-9]{3}-[0-9]{2}-[0-9]{2}$', num) else 'False'

print(phone_g("+7(920)468-00-68"))