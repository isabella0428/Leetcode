class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        tmp = 0
        for i in range(1, len(prices)):
            difference = prices[i] - prices[i - 1]
            if tmp >= 0:
                tmp += difference
                profit = max(tmp, profit)
            if tmp < 0:
                tmp = 0
        profit = max(tmp, profit)
        return profit


if __name__ == "__main__":
    a = Solution()
    print(a.maxProfit([7,1,5,3,6,4]))