class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count = 1
        ans = {}
        pointer = head
        if not pointer.next and n == 1:
            return
        if not pointer.next.next and n == 1:
            pointer.next = None
            return pointer
        if not pointer.next.next and n == 2:
            return pointer.next
        while pointer.next.next:
            start = pointer
            end = pointer.next.next
            ans[count] = [start, end]
            count += 1
            pointer = pointer.next
        count += 1
        if n == 1:
            pointer.next = None
            return head
        if count == n:
            return head.next
        remove = ans[count - n]
        start = remove[0]
        end = remove[1]
        start.next = end
        return head


if __name__ == "__main__":
    a = Solution()
    node1 = ListNode(1)
    node1.next = ListNode(2)
    node1.next.next = ListNode(3)
    pointer = a.removeNthFromEnd(node1, 2)
    while pointer:
        print(pointer.val)
        pointer = pointer.next






