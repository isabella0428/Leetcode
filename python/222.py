class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.sum = 0

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def height(root):
            if not root:
                return 0
            return 1 + height(root.left)

        if not root:
            return 0
        total_height = height(root)
        height = height(root.right)
        if height == total_height - 1:
            count = 1 << (total_height - 1) if total_height >= 1 else 1
            self.sum = count + self.countNodes(root.right)
        else:
            count = int((1 << (total_height - 2))) if total_height >= 2 else 1
            self.sum = count + self.countNodes(root.left)

        return self.sum


if __name__ == "__main__":
    a = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    print(a.countNodes(root))