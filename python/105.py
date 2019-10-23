from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        def generateTree(preorder, inorder):
            if not inorder:
                return None
            val = preorder.popleft()
            root = TreeNode(val)

            index = inorder.index(val)
            root.left = generateTree(preorder, inorder[:index])
            root.right = generateTree(preorder, inorder[index + 1:])

            return root

        return generateTree(deque(preorder), inorder)


if __name__ == "__main__":
    a = Solution()
    root = a.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])

