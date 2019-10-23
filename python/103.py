class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        stack = [[root]]
        start = 0
        while start <= len(stack):
            nodelist = stack[-1]
            tmp = []
            start += 1
            for i in range(len(nodelist)):
                node = nodelist[i]
                if node.left:
                    if node.right:
                        tmp.append(node.left)
                        tmp.append(node.right)
                    else:
                        tmp.append(node.left)
                else:
                    if node.right:
                        tmp.append(node.right)
            if not tmp:
                break
            stack.append(tmp)
        count = 0
        ret = []
        for i in range(len(stack)):
            tmp = []
            if not count % 2:
                for j in range(len(stack[i])):
                    tmp.append(stack[i][j].val)
                count += 1
            else:
                for j in range(len(stack[i]) - 1, -1, -1):
                    tmp.append(stack[i][j].val)
                count += 1
            ret.append(tmp)
        return ret


if __name__ == "__main__":
    a = Solution()
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(4)
    # root.right.left = TreeNode(15)
    root.right.right = TreeNode(5)
    print(a.zigzagLevelOrder(root))