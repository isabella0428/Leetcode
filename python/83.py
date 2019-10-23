class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        prev = head
        node = head.next
        while node:
            if node.val != prev.val:
                prev = node
                node = node.next
            else:
                prev.next = node.next
                node = prev.next
        return head


if __name__ == "__main__":
    a = Solution()
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(3)
    pointer = a.deleteDuplicates(head)
    while head:
        print(head.val)
        head = head.next

