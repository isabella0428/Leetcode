class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.path = []

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        def Path(node, strs):
            strs = strs + "->" + str(node.val) if strs != '' else str(node.val)
            if not node.left and not node.right:
                self.path.append(strs)
            if node.left:
                Path(node.left, strs[:])
            if node.right:
                Path(node.right, strs[:])

        if not root:
            return []
        Path(root, "")
        return self.path


if __name__ == "__main__":
    a = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    print(a.binaryTreePaths(root))