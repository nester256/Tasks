def read_log_file(file_name):
    with open(file_name, "r") as file:
        return {k: v.replace("\n", "") for k, v in [x.split("=") for x in file.readlines()]}
    # list_k_v = []
    # for k_v in text_in_file:
    #     list_k_v.append(k_v.split('='))
    # for k, v in list_k_v:
    #     dict_for_log[k] = v.replace("\n", "")
    # return dict_for_log


# print(read_log_file("test"))


def division_num(a, b):
    return a / b

# def user_registrator(user_login: str, user_password)
