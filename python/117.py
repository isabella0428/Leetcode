class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution1:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        # BFS
        stack = [[root]]
        start = 0
        while start < len(stack):
            nodelist = stack[-1]
            tmp = []
            for node in nodelist:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            if tmp:
                stack.append(tmp)
            start += 1
        for level in stack:
            for i in range(len(level) - 1):
                level[i].next = level[i + 1]


class Solution2:
    def connect(self, node):
        tail = dummy = TreeLinkNode(0)
        while node:
            tail.next = node.left
            if tail.next:
                tail = tail.next
            tail.next = node.right
            if tail.next:
                tail = tail.next
            node = node.next
            if not node:
                tail = dummy
                node = dummy.next


if __name__ == "__main__":
    a = Solution2()
    root = TreeLinkNode(1)
    root.left = TreeLinkNode(2)
    root.right = TreeLinkNode(3)
    root.left.left = TreeLinkNode(4)
    root.left.right = TreeLinkNode(5)
    root.right.right = TreeLinkNode(7)

    a.connect(root)




