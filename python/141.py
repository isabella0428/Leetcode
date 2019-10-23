# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution1:
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        dict = {}  # for address
        while head:
            if id(head) in dict:            #address of head
                return True  # circle
            dict[id(head)] = 1
            head = head.next
        return False


class Solution2:
    #fast runner and slow runner
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        fast_runner = head
        slow_runner = head.next
        while slow_runner != fast_runner:
            if not fast_runner:
                return False
            slow_runner = slow_runner.next
            fast_runner = fast_runner.next
        return True




