# o(n)^2
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(5)


def binaryTreePaths(root):
    queue = [] # очередь для уровней
    result = []
    queue.append(root)
    left = str(queue[0].val) + "->"
    right = str(queue[0].val) + "->"

    while (queue):
        qlen = len(queue)
        values = 0
        for i in range(qlen):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
                if node.left.left:
                    left += "{}->".format(node.left.val)
                else:
                    left += "{}".format(node.left.val)
            if node.right:
                queue.append(node.right)
                if node.right.right:
                    right += "{0}->".format(node.right.val)
                else:
                    right += "{0}".format(node.right.val)

    result.append(left)
    result.append(right)
    return result


print(binaryTreePaths(tree))