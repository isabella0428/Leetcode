class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        count = 0
        node = head
        while node.next:
            count += 1
            node = node.next
        last = node
        node.next = head
        count += 1

        step = count - k
        if step < 0:
            step += (int(abs(step) / count) + 1) * count

        step = step % count
        if step == 0:
            last.next = None
            return head
        start = head
        while step - 1 > 0:
            start = start.next
            step -= 1
        new_head = start.next
        start.next = None
        return new_head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution2:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        dicts = {}
        count, node = 0, head
        while node:
            count += 1
            dicts[count] = node
            node = node.next
        k = k % count
        if k == 0:
            return head
        node1, new_head, node2 = dicts[count - k], dicts[count - k + 1], dicts[count]
        node1.next = None
        node2.next = head
        return new_head


if __name__ == "__main__":
    a = Solution2()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    pointer = a.rotateRight(head, 2)
    while pointer:
        print(pointer.val)
        pointer = pointer.next


