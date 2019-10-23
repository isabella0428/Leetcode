class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        nodeA, nodeB = headA, headB
        FlagA, FlagB = False, False
        while nodeA and nodeB:
            if nodeA == nodeB:
                return nodeA
            nodeA = nodeA.next
            nodeB = nodeB.next
            if not nodeA and not FlagA:
                nodeA = headB
                FlagA = True
            if not nodeB and not FlagB:
                nodeB = headA
                FlagB = True

        return None


if __name__ == "__main__":
    a = Solution()
    headA = ListNode(4)
    headA.next = ListNode(1)
    headA.next.next = ListNode(8)
    headA.next.next.next = ListNode(4)
    headA.next.next.next.next = ListNode(5)
    headB = ListNode(5)
    headB.next = ListNode(0)
    headB.next.next = ListNode(1)
    headB.next.next.next = headA.next.next
    print(a.getIntersectionNode(headA, headB).val)