# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSubtree(self, s: 'TreeNode', t: 'TreeNode') -> 'bool':
        def same(s, t):
            if not s and not t:
                return True
            if not s or not t:
                return False
            if s.val != t.val:
                return False
            return same(s.left, t.left) and same(s.right, t.right)
        if not s and not t:
            return True
        if not s or not t:
            return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t) or same(s, t)