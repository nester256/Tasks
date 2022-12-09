
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Объявляем наше дерево :)
tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.left.left = TreeNode(7)
tree.left.right = TreeNode(15)


def averageTreeBinary(root: TreeNode):
    queue = []                      # очередь для уровней
    result = []                     # список результатов
    queue.append(root)              # добавляем голову нашей змеи :)

    while (queue):                  # Пока наше дерево есть мы идём по его уровням
        qlen = len(queue)           # длинна очереди (т.е сколько на этом уровне есть ячеек)
        values = 0                  # сюда будем добавялть значения всех ячеек уровня
        for i in range(qlen):       # цикл по всем ячейкам на уровне
            node = queue.pop(0)     # Убираем ячейку из очереди и работаем с ней
            values += node.val      # Добавляем значение ячейки
            # print(node.val, qlen)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)    # Ищем более низкие уровни и добавляем их в очередь
        result.append(values / qlen)        # добавляем среднее значене нашего уровня
    return result                           # Возвращаем результат наших вычислений


print(averageTreeBinary(tree))