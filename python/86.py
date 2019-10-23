class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: 'ListNode', x: 'int') -> 'ListNode':
        num = []
        while head:
            num.append(head.val)
            head = head.next
        loc = 0
        for i in range(len(num)):
            d = num[i]
            if d < x:
                num = num[:i] + num[i + 1:]
                num.insert(loc, d)
                loc += 1
        node = prev = ListNode(0)
        for item in num:
            node.next = ListNode(item)
            node = node.next
        return prev.next


if __name__ == "__main__":
    a = Solution()
    node = head = ListNode(1)
    val = [4, 3, 2, 5, 2]
    for item in val:
        node.next = ListNode(item)
        node = node.next
    node = a.partition(head, 3)
    while node:
        print(node.val)
        node = node.next