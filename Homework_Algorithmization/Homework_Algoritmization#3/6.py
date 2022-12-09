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
    def findDepth(root):
        if root is None:
            return 0

        return 1 + max(findDepth(root.left), findDepth(root.right))

    if root is None:
        return 0
    left = findDepth(root.left)
    right = findDepth(root.right)
    left_diameter = diameterOfBinaryTree(root.left)
    right_diameter = diameterOfBinaryTree(root.right)

    return max(left + right, max(left_diameter, right_diameter))


print(diameterOfBinaryTree(tree_2))