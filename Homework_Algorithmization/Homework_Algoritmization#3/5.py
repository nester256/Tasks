# o(n)^2
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.right = TreeNode(5)
                                        # Объявляем дерево


def binaryTreePaths(root):
    queue = []                              # очередь для уровней
    result = []                             # сюда будем записывать результат
    queue.append(root)                      # добавляем начало нашего дерева :)
    left = str(queue[0].val) + "->"         # добавляем первое значение в список левых значений
    right = str(queue[0].val) + "->"        # добавляем первое значение в список правых значений

    while (queue):                          # Пока наше дерево есть мы идём по его уровням
        qlen = len(queue)                   # длинна очереди (т.е сколько на этом уровне есть ячеек)
        for i in range(qlen):               # цикл по всем ячейкам на уровне
            node = queue.pop(0)             # Убираем ячейку из очереди и работаем с ней
            if node.left:                   # Если есть слева
                queue.append(node.left)     # Добавляем значение в очередь
                if node.left.left:          # Если есть слева слева значение
                    left += "{}->".format(node.left.val)    # То добавляем значение слева его в список с ->
                else:                                       # Если нет
                    left += "{}".format(node.left.val)      # То добаялем без штуки
            if node.right:                                  # Всё то же самое с правой веткой
                queue.append(node.right)
                if node.right.right:
                    right += "{0}->".format(node.right.val)
                else:
                    right += "{0}".format(node.right.val)

    result.append(left)                                     # Добавляем левую ветку
    result.append(right)                                    # Добавляем правую ветку
    return result                                           # Возвращаем результат


print(binaryTreePaths(tree))