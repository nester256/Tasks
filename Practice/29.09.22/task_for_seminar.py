# 1 хештеги
def does_hashtag(str_1):
    return "#" + "".join([str(s.capitalize()) for s in str_1.split(" ")])


# print(does_hashtag("привет пока"))
def removed(lst):
    return "пока живи" if lst.count(1) / len(lst) >= 0.8 else "отчислен"


def go_to_NSWE(list_1):
    dict_removed = {"E": "W", "W": "E", "S": "N", "N": "S"}
    run = True
    while run:
        run = False
        for i in range(1, len(list_1)):
            if list_1[i] == dict_removed[list_1[i - 1]]:
                list_1.pop(i)
                list_1.pop(i - 1)
                run = True
                break
    return list_1



