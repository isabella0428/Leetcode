class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
        node = dummy = ListNode(-1)
        dummy.next = head
        ahead = head
        while ahead:
            if ahead.val == val:
                node.next = ahead.next
                ahead = node.next
            else:
                node = node.next
                ahead = ahead.next
        return dummy.next


