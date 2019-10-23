class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.sum = 0

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def traversal(tmp, root):
            if not root:
                return
            if not root.left and not root.right:
                tmp += str(root.val)
                self.sum += int(tmp)
                return
            tmp += str(root.val)
            traversal(tmp, root.left)
            traversal(tmp, root.right)

        if not root:
            return 0
        tmp = ''
        traversal(tmp, root)
        return self.sum


if __name__ == "__main__":
    a = Solution()
    root = TreeNode(4)
    root.left = TreeNode(9)
    root.right = TreeNode(0)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(1)
    print(a.sumNumbers(root))

