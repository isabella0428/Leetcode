class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.left = []
        self.right = []


    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        lval = rval = True
        if not root:
            return True
        if self.left:                       #ought to be bigger
            if root.val <= max(self.left):
                return False
        if self.right:
            if root.val >= min(self.right):
                return False
        if root.left:
            self.right.append(root.val)
            lval = self.isValidBST(root.left)
            self.right = self.right[:-1]
        if root.right:
            self.left.append(root.val)
            rval = self.isValidBST(root.right)
            self.left = self.left[:-1]
        return lval and rval and True


if __name__ == "__main__":
    a = Solution()
    root = TreeNode(1)
    root.left = TreeNode(1)
    # root.right = TreeNode(4)
    # root.right.left = TreeNode(3)
    # root.right.right = TreeNode(6)
    print(a.isValidBST(root))

