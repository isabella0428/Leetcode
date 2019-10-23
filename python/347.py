from collections import Counter
import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)


if __name__ == '__main__':
    a = Solution()
    print(a.topKFrequent([5,2,5,3,5,3,1,1,3],
2))

