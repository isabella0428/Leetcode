class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_list, l2_list = [], []
        while l1:
            l1_list.append(l1)
            l1 = l1.next
        while l2:
            l2_list.append(l2)
            l2 = l2.next
        carry, ret = 0, []
        while l1_list or l2_list or carry:
            val = carry
            item1 = l1_list.pop().val if l1_list else 0
            item2 = l2_list.pop().val if l2_list else 0
            val = item1 + item2 + carry
            carry, val = divmod(val, 10)
            ret.append(ListNode(val))
        cur = dummy = ListNode(-1)
        while ret:
            cur.next = ret.pop()
            cur = cur.next
        return dummy.next



