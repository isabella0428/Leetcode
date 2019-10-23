class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.route = []

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ans = []
        self.pathSum_ans(root, sum, ans)
        return self.route

    def pathSum_ans(self, root, sum, ans):
        if not root:
            return
        if not root.left and not root.right:
            if sum == root.val:
                ans.append(root.val)
                self.route.append(ans)
                return
            else:
                return

        sum -= root.val
        ans.append(root.val)
        self.pathSum_ans(root.left, sum, ans[:])
        self.pathSum_ans(root.right, sum, ans[:])


if __name__ == "__main__":
    a = Solution()
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    print(a.pathSum(root, 22))