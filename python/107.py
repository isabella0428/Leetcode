import queue
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = []
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            levelNodes, levelLength = [], q.qsize()
            for i in range(levelLength):
                out = q.get()
                levelNodes.append(out.val)
                if out.left:
                    q.put(out.left)
                if out.right:
                    q.put(out.right)
            ans.insert(0, levelNodes)
        return ans



if __name__ == "__main__":
    a = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(a.levelOrderBottom(root))





