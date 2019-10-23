class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key = lambda x: x[1])
        erase = 0
        end = float('-inf')
        for item in intervals:
            if item[0] > end:
                end = item[1]
            else:
                erase += 1
        return erase


if __name__ == "__main__":
    a = Solution()
    print(a.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))

