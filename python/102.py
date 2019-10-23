class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        stack = [[root]]
        ans = [[root.val]]
        start = 1
        while start <= len(stack):
            nodelist = stack[-1]
            level = []
            tmp = []
            for node in nodelist:
                if node.left:
                    level.append(node.left)
                    tmp.append(node.left.val)
                if node.right:
                    level.append(node.right)
                    tmp.append(node.right.val)
            if len(tmp) != 0:
                start += 1
                ans.append(tmp)
                stack.append(level)
            else:
                break
        return ans


if __name__ == "__main__":
    a = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(a.levelOrder(root))





