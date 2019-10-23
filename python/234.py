class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        def reverse(node):
            prev, cur, now = node, node.next, node.next
            prev.next = None
            while now:
                now = now.next
                cur.next = prev
                prev = cur
                cur = now
            return prev

        if not head or not head.next:
            return True
        dict, count = {}, 0
        node = head
        while node:
            count += 1
            dict[count] = node
            node = node.next
        if count % 2:
            start = int((count + 1) / 2) + 1
        else:
            start = int(count / 2) + 1
        rev = reverse(dict[start])
        while rev:
            if rev.val != head.val:
                return False
            rev = rev.next
            head = head.next
        return True


if __name__ == "__main__":
    a = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    print(a.isPalindrome(head))