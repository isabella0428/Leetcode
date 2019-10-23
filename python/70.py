class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt0 = 0
        cnt1 = 1
        for i in range(n):
            tmp = cnt0
            cnt0 = cnt1
            cnt1 += tmp
        return cnt1


if __name__ == "__main__":
    a = Solution()
    print(a.climbStairs(10))