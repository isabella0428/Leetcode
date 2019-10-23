class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        lheight = self.minDepth(root.left)
        rheight = self.minDepth(root.right)
        if lheight == 0:
            return rheight + 1
        if rheight == 0:
            return lheight + 1
        return min(lheight, rheight) + 1


if __name__ == "__main__":
    a = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    print(a.minDepth(root))
