class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        sum -= root.val
        if not root.left and not root.right:
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)


class Solution2:                        #DFS
    def hasPathSum(self, root, sum):
        if not root:
            return False
        stack = [(root, sum - root.val)]
        while len(stack) != 0:
            node, sum = stack.pop()
            if not node.left and not node.right and sum == 0:
                return True
            if node.right:
                stack.append((node.right, sum - node.right.val))
            if node.left:
                stack.append((node.left, sum - node.left.val))
        return False


class Solution3:
    def hasPathSum(self, root: 'TreeNode', sum: 'int') -> 'bool':
        def DFS(node, tmp):
            nonlocal possible
            if not node.left and not node.right:
                possible.append(tmp + node.val)
                return
            if node.left:
                DFS(node.left, node.val + tmp)
            if node.right:
                DFS(node.right, node.val + tmp)

        if not root:
            return False
        possible = []
        DFS(root, 0)
        return sum in possible


if __name__ == "__main__":
    a = Solution3()
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right = TreeNode(8)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    print(a.hasPathSum(root, 22))