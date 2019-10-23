class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        def reverse(start, end, times):
            prev = None
            node = start
            for i in range(times):
                cur = node
                node = node.next
                cur.next = prev
                prev = cur
            return cur, start

        ahead = node = dummy = ListNode(-1)
        dummy.next = head
        for i in range(n - m):
            if ahead:
                ahead = ahead.next
            else:
                return False
        for i in range(m - 1):
            node = node.next
            ahead = ahead.next
        prev = node
        end = ahead.next.next
        prev.next, tmp_end = reverse(node.next, ahead.next, n - m + 1)
        tmp_end.next = end
        return dummy.next


if __name__ == "__main__":
    a = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    # head.next.next = ListNode(3)
    # head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)
    pointer = a.reverseBetween(head, 1, 2)
    while pointer:
        print(pointer.val)
        pointer = pointer.next