class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1(object):
    def __init__(self):
        self.traversal = []

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        vallist = self.preorder(root)
        root.left = None
        cur = root
        vallist = vallist[1:]
        for item in vallist:
            cur.right = TreeNode(item)
            cur.left = None
            cur = cur.right

    def preorder(self, root):
        if not root:
            return
        self.traversal.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)
        return self.traversal


class Solution2:
    def __init__(self):
        self.prev = None

    def flatten(self, root):
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root


if __name__ == "__main__":
    a = Solution2()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)
    flattened_root = a.flatten(root)


