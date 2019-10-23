class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        n = len(prices)
        if n < 2:
            return 0
        buy = [0 for i in range(n)]
        s1, s2, sell = buy[:], buy[:], buy[:]
        buy[0], s1[0] = -prices[0], -prices[0]
        for i in range(1, n):
            buy[i] = s2[i - 1] - prices[i]
            s1[i] = max(s1[i - 1], buy[i - 1])
            s2[i] = max(s2[i - 1], sell[i - 1])
            sell[i] = max(buy[i - 1], s1[i - 1]) + prices[i]
        return max(sell[n - 1], s2[n - 1])


if __name__ == "__main__":
    a = Solution()
    print(a.maxProfit([1,2,4]))