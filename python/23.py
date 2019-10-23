from queue import PriorityQueue as PQ


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        pq = PQ()
        cur = dummy = ListNode(0)     #dummy headnode
        count = 0
        zero_count = 0
        for i in lists:
            if i:
                pq.put((i.val, count))  #when the first one is equal,compare the second one
                zero_count += 1
            count += 1
        if zero_count == 0:
            return
        while 1:
            mini, loc = pq.get()          #value, node of min-terms
            cur.next = ListNode(mini)
            cur = cur.next
            if lists[loc]:
                lists[loc] = lists[loc].next
            if lists[loc]:
                pq.put((lists[loc].val, loc))
            if pq.empty():
                return dummy.next


class Solution2:
    def mergeKLists(self, lists: 'List[ListNode]') -> 'ListNode':
        que, dummy = PQ(), ListNode(-1)
        cur = dummy
        count = 0
        for node in lists:
            if node:
                que.put((node.val, count))
            count += 1
        while not que.empty():
            val, loc = que.get()
            cur.next = ListNode(val)
            cur = cur.next
            if lists[loc].next:
                lists[loc] = lists[loc].next
                que.put((lists[loc].val, loc))
        return dummy.next


if __name__ == "__main__":
    node1 = ListNode(-1)
    node1.next = ListNode(5)
    node1.next.next = ListNode(11)
    node2 = ListNode(6)
    node2.next = ListNode(10)
    node3 = ListNode(2)
    node3.next = ListNode(6)
    a = Solution2()
    pointer = a.mergeKLists([[], node1, [], node2])
    while pointer:
        print(pointer.val)
        pointer = pointer.next


