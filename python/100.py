class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.tmp = ""

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        self.Fill(p)
        self.Fill(q)
        self.PreOrder(p)
        p_pre = self.tmp
        self.tmp = ""
        self.PreOrder(q)
        q_pre = self.tmp
        self.tmp = ""
        self.InOrder(p)
        p_in = self.tmp
        self.tmp = ""
        self.InOrder(q)
        q_in = self.tmp
        if p_pre in q_pre and len(p_pre) == len(q_pre):
            if p_in in q_in and len(p_in) == len(q_in):
                return True
        return False


    def PreOrder(self, p):
        if p:
            self.tmp = self.tmp + str(p.val)
        else:
            return
        self.PreOrder(p.left)
        self.PreOrder(p.right)


    def InOrder(self, q):
        if not q:
            return
        self.InOrder(q.left)
        self.tmp = self.tmp + str(q.val)
        self.InOrder(q.right)


    def Fill(self, p):
        if p:
            if p.left and not p.right:
                p.right = TreeNode('@')
            if p.right and not p.left:
                p.left = TreeNode('@')
        else:
            return
        self.Fill(p.left)
        self.Fill(p.right)



