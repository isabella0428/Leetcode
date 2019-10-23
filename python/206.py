class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Be very careful that n1's next must point to Ø
        if not head or not head.next:
            return head
        node = head
        new_head = head.next
        node.next = None
        while new_head:
            cur_head = new_head
            new_head = new_head.next
            cur_head.next = node
            node = cur_head
        return cur_head


if __name__ == "__main__":
    a = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next =ListNode(4)
    head.next.next.next.next = ListNode(5)
    pointer = a.reverseList(head)
    while pointer:
        print(pointer.val)
        pointer = pointer.next