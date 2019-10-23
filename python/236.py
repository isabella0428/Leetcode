class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        ans = None

        def findAncestor(root, p, q):
            nonlocal ans
            if not root:
                return False
            mid = root == p or root == q
            left = findAncestor(root.left, p, q)
            right = findAncestor(root.right, p, q)
            if mid + left + right >= 2:
                ans = root
            return mid or left or right

        findAncestor(root, p, q)
        return ans

class Solution1:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #using parent nodes
        stack = [root]
        parent = {root: None}
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ancestor = set()    #ancestor for p
        while p:
            ancestor.add(parent[p])
            p = parent[p]
        while q not in ancestor:
            q = parent[q]
        return q


class Solution2:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """






if __name__ == "__main__":
    a = Solution1()
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    print(a.lowestCommonAncestor(root,root.left.right.left, root.left.right.right).val)