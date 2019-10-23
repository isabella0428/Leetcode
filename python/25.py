class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    # reverse the linked list in one pass
    def Reverse(self, start, end):    
        if start == end:
            return start
        to_do = start.next
        reversed = start
        reversed.next = None
        end.next = None
        while to_do:
            tmp = to_do
            to_do = to_do.next
            tmp.next = reversed
            reversed = tmp
        return reversed, start


    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:
            return head
        num = 0
        start = end = head
        count = 0
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while end:
            count = count + 1
            if count % k == 0:
                tmp = end.next
                new_start, new_end = self.Reverse(start, end)
                prev.next = new_start
                prev = new_end
                if count / k == 1:
                    head = new_start
                if end:
                    start = end = tmp
                    new_end.next = tmp
                    continue
                else:
                    return head
            end = end.next
        return head


class Solution2:
    def reverseKGroup(self, head: 'ListNode', k: 'int') -> 'ListNode':
        def reverse(node, end):
            prev, new = None, node
            while new != end:
                cur = new
                new = new.next
                cur.next = prev
                prev = cur
            return prev, node

        dummy = ListNode(-1)
        dummy.next = head
        count, start, prev = 0, [], dummy
        node = head
        if k < 2:
            return head
        while node:
            count += 1
            if count % k == 1:
                start.append(node)
            if count % k == 0:
                node = node.next
                prev.next, prev = reverse(start[-1], node)
                prev.next = node
                continue
            node = node.next
        return dummy.next


if __name__ == "__main__":
    a = Solution2()
    tmp = node1 = ListNode(1)
    tmp.next = ListNode(2)
    tmp = tmp.next
    tmp.next = ListNode(3)
    tmp = tmp.next
    tmp.next = ListNode(4)
    tmp = tmp.next
    tmp.next = ListNode(5)

    pointer = a.reverseKGroup(node1, 3)
    while pointer:
        print(pointer.val)
        pointer = pointer.next

