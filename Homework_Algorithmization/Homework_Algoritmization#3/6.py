# o(n) or o(n)^2 (в зависимости от сложности)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
tree_2 = TreeNode(1, TreeNode(2))

# tree = TreeNode(1)
# tree.left = TreeNode(2)
# tree.right = TreeNode(3)
# tree.left.left = TreeNode(4)
# tree.left.right = TreeNode(5)


def diameterOfBinaryTree(root: TreeNode) -> int:
    def findDepth(root):        # Данный метод ищет глубину ветки используя рекурсию
        if root is None:       # Если ячейка нулевая то возвращает 0
            return 0

        return 1 + max(findDepth(root.left), findDepth(root.right))
                                # С помощью рекурсии находит максимальную глубину ветки + 1 так как от начала тоже есть путь

    if root is None:                                             # Если ячейка нулевая то возвращает 0
        return 0
    left = findDepth(root.left)                                   # Глубина левой ветки
    right = findDepth(root.right)                                 # Глубина правой ветки
    left_diameter = diameterOfBinaryTree(root.left)              # Рекурсия для левой ветки что бы найти диаметр
    right_diameter = diameterOfBinaryTree(root.right)            # Рекурсия для правой ветки что бы найти диаметр

    return max(left + right, max(left_diameter, right_diameter))  # Возвращает диаметр дерева или же ветвей (зависит от этапа рекурсии)


print(diameterOfBinaryTree(tree_2))