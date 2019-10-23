class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def height(self, node):
        if not node:
            return 0

        lh = self.height(node.left)
        rh = self.height(node.right)

        return max(lh, rh) + 1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        """
        Python3 program to check if a tree is height-balanced
        """

        if not root:
            return True
        if self.isBalanced(root.left) and self.isBalanced(root.right):
            if abs(self.height(root.left) - self.height(root.right)) <= 1:
                return True
        return False


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.left.left = TreeNode(8)
    a = Solution()
    if a.isBalanced(root):
        print("Tree is balanced")
    else:
        print("Tree is not balanced")