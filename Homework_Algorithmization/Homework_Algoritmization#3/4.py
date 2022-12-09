# o(n)
class LinkedList:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


head = LinkedList(1, LinkedList(0, LinkedList(1)))
                                # Объявляем нашу змею :)


def initList(head: LinkedList):
    res = ""                    # Результат будем записывать сюда
    while head:                 # Идём пока змея не кончится
        res += str(head.val)    # Записываем значение элемента змеи
        head = head.next        # Двигаемся дальше по змее
    return (int(res, 2))        # Переводим наше значение по двочиной системе исчисления и возвращаем


print(initList(head))
