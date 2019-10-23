class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        node1 = l1
        node2 = l2
        num = 0
        carry = 0
        startNode = ListNode(-1)
        curNode = ListNode(-1)

        while (1):
            if node1.val == 0 and node2.val == 0 and carry == 0 :
                return startNode

            val = node1.val + node2.val + carry
            carry = int(val / 10)
            val = val % 10
            num = num + 1

            if startNode.val == -1:
                startNode = ListNode(val)
                curNode = startNode

            else:
                curNode = startNode
                for p in range(num - 2):
                    curNode = curNode.next
                curNode.next = ListNode(val)

            if node1.next != None:
                node1 = node1.next
            else:
                node1.val = 0

            if node2.next != None:
                node2 = node2.next
            else:
                node2.val = 0

class Solution1:
    def addTwoNumbers(self, l1, l2):
        dummyHead = ListNode(-1)
        carry = 0
        p1 = l1
        p2 = l2
        cur = dummyHead

        while p1 != None or p2 != None:
            x = p1.val if p1 != None else 0
            y = p2.val if p2 != None else 0
            sum = x + y + carry
            carry = int(sum / 10)
            sum = sum % 10

            cur.next = ListNode(sum)
            cur = cur.next

            if p1 != None:
                p1 = p1.next
            if p2 != None:
                p2 = p2.next

        if carry > 0:
            cur.next = ListNode(1)
        return dummyHead.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


if __name__ == "__main__":
    a = ListNode(2)
    tmp = ListNode(4)
    a.next = tmp
    tmp.next = ListNode(3)

    b = ListNode(5)
    tmp1 = ListNode(6)
    b.next = tmp1
    tmp1.next = ListNode(4)

    startNode = ListNode(-1)

    c = Solution3()
    startNode = c.addTwoNumbers(a, b)
    while startNode.next != None:
        print(startNode.val)
        startNode = startNode.next

    print(startNode.val)
