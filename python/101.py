class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):        #BFS
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = [[root]]
        start = 1
        while start <= len(stack):
            nodelist = stack[-1]
            tmp = []
            level = []
            for node in nodelist:
                if not node:
                    continue
                lval = None if not node.left else node.left.val
                rval = None if not node.right else node.right.val
                tmp.append(lval)
                tmp.append(rval)
                level.append(node.left)
                level.append(node.right)
            if tmp[::-1] == tmp:
                count = 0
                for item in tmp:
                    if item != None:
                        count += 1
                        break
                if count == 0:
                    break
                stack.append(level)
                start += 1
            else:
                return False
        return True


if __name__ == "__main__":
    a = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(3)
    print(a.isSymmetric(root))