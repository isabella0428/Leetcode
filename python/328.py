class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type node: ListNode
        :rtype: ListNode
        """
        cur_e = e_node = ListNode(-1)
        cur_o = o_node = ListNode(-1)
        cnt = 0
        node = head
        if not head or head and not head.next or head and head.next and not head.next.next:
            return head
        while node:
            cnt += 1
            prev = node
            node = node.next
            if cnt % 2:
                prev.next = None
                cur_o.next = prev
                cur_o = cur_o.next
                if node and not node.next or not node:
                    cur_o.next = e_node.next
            else:
                prev.next = None
                cur_e.next = prev
                cur_e = cur_e.next
                if node and not node.next or not node:
                    cur_e.next = None
        if cnt <= 2:
            return head
        return o_node.next


if __name__ == "__main__":
    a = Solution()
    node = ListNode(1)
    node.next = ListNode(1)
    # node.next.next = ListNode(3)
    # node.next.next.next = ListNode(4)
    # node.next.next.next.next = ListNode(5)
    pointer = a.oddEvenList(node)
    while pointer:
        print(pointer.val)
        pointer = pointer.next