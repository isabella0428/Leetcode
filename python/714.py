class Solution1:
    def maxProfit(self, prices: 'List[int]', fee: 'int') -> 'int':
        n = len(prices)
        if n < 2:
            return 0
        buy = [0 for i in range(n)]
        sell, s1, s2 = buy[:], buy[:], buy[:]
        buy[0], s1[0] = -prices[0], -prices[0]
        for i in range(1, n):
            buy[i] = max(sell[i - 1], s2[i - 1]) - prices[i]
            sell[i] = max(buy[i - 1], s1[i - 1]) + (prices[i] - fee)
            s2[i] = max(sell[i - 1], s2[i - 1])
            s1[i] = max(buy[i - 1], s1[i - 1])
        return max(max(buy), max(sell), s1[n - 1], s2[n - 1])


class Solution2(object):
    def maxProfit(self, prices, fee):
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        return cash


if __name__ == "__main__":
    a = Solution2()
    print(a.maxProfit([7,6,5,4,3,2,1], 2))