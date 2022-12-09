
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.left.left = TreeNode(7)
tree.left.right = TreeNode(15)


def averageTreeBinary(root: TreeNode):
    queue = []
    result = []
    queue.append(root)

    while (queue):
        qlen = len(queue)
        values = 0
        for i in range(qlen):
            node = queue.pop(0)
            values += node.val
            # print(node.val, qlen)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(values / qlen)
    return result


print(averageTreeBinary(tree))