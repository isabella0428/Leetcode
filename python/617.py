class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: 'TreeNode', t2: 'TreeNode') -> 'TreeNode':
        def merge(node, nodeA, nodeB):
            if not nodeA and not nodeB:
                return
            val1 = nodeA.val if nodeA else 0
            val2 = nodeB.val if nodeB else 0
            node.val = val1 + val2
            if nodeA and nodeA.left or nodeB and nodeB.left:
                lnode1 = nodeA.left if nodeA and nodeA.left else None
                lnode2 = nodeB.left if nodeB and nodeB.left else None
                node.left = TreeNode(-1)
                merge(node.left, lnode1, lnode2)
            if nodeA and nodeA.right or nodeB and nodeB.right:
                rnode1 = nodeA.right if nodeA and nodeA.right else None
                rnode2 = nodeB.right if nodeB and nodeB.right else None
                node.right = TreeNode(-1)
                merge(node.right, rnode1, rnode2)

        if not t1 and not t2:
            return None
        head = TreeNode(-1)
        merge(head, t1, t2)
        return head


