class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == [] and l2 == []:
            return
        if l1.val == None:
            return l2
        if l2.val == None:
            return l1
        node = ListNode(0)
        tmp = node
        node1 = l1
        node2 = l2
        while node1 and node2:
            if node1.val < node2.val:
                tmp.next = ListNode(node1.val)
                tmp = tmp.next
                node1 = node1.next
            else:
                tmp.next = ListNode(node2.val)
                tmp = tmp.next
                node2 = node2.next
        tmp.next = node1 or node2
        return node.next



if __name__ == "__main__":
    a = Solution()
    node1 = ListNode(1)
    node1.next = ListNode(2)
    node1.next.next = ListNode(4)
    node2 = ListNode(1)
    node2.next = ListNode(3)
    node2.next.next = ListNode(4)
    node = a.mergeTwoLists(node1, node2)
    while node:
        print(node.val)
        node = node.next



