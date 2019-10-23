class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        node, head = root, root
        count = 0
        while node:
            count += 1
            node = node.next
        size = [int(count / k) for i in range(k)]
        for i in range(count % k):
            size[i] += 1
        ret = []
        dummy = ListNode(-1)
        dummy.next = head
        cur_size, cur = 0, 0
        node = head
        while node:
            if cur == 0:
                ret.append(node)
            cur += 1
            if cur == size[cur_size]:
                if not node.next:
                    break
                prev = node
                node = node.next
                prev.next = None
                cur_size += 1
                cur = 0
                continue
            node = node.next
        while len(ret) < k:
            ret.append(None)
        return ret


if __name__ == "__main__":
    a = Solution()
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(3)
    root.next.next.next = ListNode(4)
    print(a.splitListToParts(root, 5))


