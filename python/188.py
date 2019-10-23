class Solution:
    def maxProfit(self, k: 'int', prices: 'List[int]') -> 'int':
        n = len(prices)
        if k > n / 2:
            # normal stock problem
            maxProfit = 0
            for i in range(1, len(prices)):
                delta = prices[i] - prices[i - 1]
                if delta > 0:
                    maxProfit += delta
            return maxProfit
        else:
            maxProfit = [[0 for j in range(n)] for i in range(1 + k)]
            for i in range(1, 1 + k):
                local_Max = maxProfit[i - 1][0] - prices[0]
                for j in range(1, n):
                    maxProfit[i][j] = max(maxProfit[i][j - 1], local_Max + prices[j])
                    local_Max = max(local_Max, maxProfit[i - 1][j] - prices[j])
            return maxProfit[k][n - 1]


if __name__ == "__main__":
    a = Solution()
    print(a.maxProfit(2, [6, 1, 3, 2, 4, 7]))