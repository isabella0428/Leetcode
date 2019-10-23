class Solution:
    # greedy: make sure that the former one's end
    # may be included in the latter one
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda i: i[1])
        arrow = 0
        cur = float('-inf')
        for item in points:
            if cur < item[0]:
                arrow += 1
                cur = item[1]
        return arrow

if __name__ == "__main__":
    a = Solution()
    print(a.findMinArrowShots([[10,16], [2,8], [1,6], [7,12]]))
