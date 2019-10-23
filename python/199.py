class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        stack = [[root]]
        start = 0
        ret = []
        while start < len(stack):
            tmp = []
            for node in stack[start]:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            if not tmp:
                break
            stack.append(tmp)
            start += 1
        for i in range(len(stack)):
            ret.append(stack[i][-1].val)
        return ret


if __name__ == "__main__":
    a = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    print(a.rightSideView(root))

