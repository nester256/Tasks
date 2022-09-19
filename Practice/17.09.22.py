# Bingo

# Это функция проверки
def leader(n):
    l_1 = []
    for i in range(1, n + 1):
        l_1.append(i)
    random.shuffle(l_1)
    while True:
        answer = input('Is game over?')
        if answer == 'yes':
            break
        if len(l_1) == 0:
            print('numbers are over')
            break
        print(l_1.pop())


import random


# Генерация карточки 5 х 5
def gen_card(n):
    list_1 = []
    while len(list_1) < 25:
        a = random.randint(1, n)
        if not (a in list_1):
            list_1.append(a)
    resolve = []
    for i in range(5):
        resolve.append(list_1[i * 5: (i + 1) * 5])
    return resolve

#Проверить карточку
def end_test(card):
    for string in card:
        if string.count('X') == 5:
            return True
    for i in range(len(card[0])):
        lst = []
        for j in range(len(card)):
            lst.append(card[j][i])
        if lst.count('X') == 5:
            return True
    return False

# Принять карточку
def take_card(card):
    print(card)
    while True:
        user_input = input("Введите число (q - для выхода): ")
        if user_input == "q":
            break
        num = int(user_input)
        for line in card:
            for element in range(len(line)):
                if line[element] == num:
                    line[element] = "X"
                    break
        print(card)
        if end_test(card):
            print("BINGO")
            return



take_card(gen_card(90))


