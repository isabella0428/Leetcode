class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        memo = {}

        def height(node):
            nonlocal memo
            if not node:
                return 0
            if node in memo:
                return memo[node]
            memo[node] = 1 + max(height(node.left), height(node.right))
            return memo[node]

        if not root or not root.left and not root.right:
            return 0
        depth, stack, i = 1, [root], 0
        while i < len(stack):
            node = stack[i]
            i += 1
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        while stack:
            node = stack.pop()
            depth = max(height(node.left) + height(node.right), depth)
        return depth


if __name__ == "__main__":
    a = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(a.diameterOfBinaryTree(root))






