# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        def BinarySearch(left, right):
            if left == right and isBadVersion(left):
                return left
            if not isBadVersion(left) and isBadVersion(right) and right - left == 1:
                return right
            mid = (left + right) >> 1
            if isBadVersion(mid):
                return BinarySearch(left, mid)
            else:
                return BinarySearch(mid, right)

        return BinarySearch(1, n)
