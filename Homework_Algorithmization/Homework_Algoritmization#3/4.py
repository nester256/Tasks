# o(n)
class LinkedList:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


head = LinkedList(1, LinkedList(0, LinkedList(1)))


def initList(head: LinkedList):
    res = ""
    while head:
        res += str(head.val)
        head = head.next
    return (int(res, 2))


print(initList(head))
