import math


class Solution1:
    #uses sqrt
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for a in range(int(math.sqrt(c)) + 1):
            b = c - a ** 2
            if int(math.sqrt(b)) ** 2 == b:
                return True
        return False

class Solution2:
    #BinarySearch
    def judgeSquareSum(self, c):
        def BinarySearch(start, end, b):
            if start > end:
                return False
            mid = int((start + end)/ 2)
            if mid ** 2 > b:
                end = mid - 1
            if mid ** 2 < b:
                start = mid + 1
            return True

        for i in range(int(math.sqrt(c)) + 1):
            b = c - i ** 2
            start = 0
            end = int(math.sqrt(c))
            if BinarySearch(start, end, b):
                return True
        return False


if __name__ == "__main__":
    a = Solution2()
    print(a.judgeSquareSum(1000000))