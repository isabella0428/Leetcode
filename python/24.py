class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:    return
        if head.next == None:
            return head
        dummy = ListNode(0)         #set a dummy node for simplification
        dummy.next = head
        node = dummy
        while 1:
            first = node.next
            end = node.next.next
            first.next = end.next
            node.next = end
            end.next = first
            if not node or not node.next or not node.next.next:
                return dummy.next
            node = node.next.next
            if not node or not node.next or not node.next.next:
                return dummy.next
        return dummy.next


class Solution2:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        node = head
        while node and node.next:
            node1, node2 = node, node.next
            node = node.next.next
            prev.next = node2
            node2.next = node1
            prev = node1
            node1.next = node
        if not node:
            node1.next = None
        return dummy.next


if __name__ == "__main__":
    a = Solution2()
    node1 = ListNode(1)
    node1.next = ListNode(2)
    node1.next.next = ListNode(3)
    # node1.next.next.next = ListNode(4)
    pointer = a.swapPairs(node1)
    while pointer:
        print(pointer.val)
        pointer = pointer.next
