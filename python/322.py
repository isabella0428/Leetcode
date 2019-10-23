class Solution1:
    def coinChange(self, coins: 'List[int]', amount: 'int') -> 'int':
        # dp
        memo = [-1 for i in range(1 + amount)]
        memo[0] = 0
        for i in range(1, amount + 1):
            if i in coins:
                memo[i] = 1
                continue
            if i == 1:
                continue
            tmp = [1 + memo[i - j] for j in coins if i >= j and memo[i - j] != -1]
            if tmp:
                memo[i] = min(tmp)
        return memo[amount]


class Solution2:
    def coinChange(self, coins: 'List[int]', amount: 'int') -> 'int':
        """
        :type coins: List[int]
        :type amount: int
        :rtype int
        """
        # complete backpack problem
        if amount == 0:
            return 0
        dp = [-1 for i in range(1 + amount)]
        dp[0] = 0
        coins.sort()
        for i in range(len(coins)):
            coin = coins[i]
            if coin <= amount:
                dp[coin] = 1
            else:
                coins = coins[:i]
                break

        for v in range(1, 1 + amount):
            for coin in coins:
                if v >= coin:
                    if dp[v - coin] != -1:
                        if dp[v] == -1:
                            dp[v] = dp[v - coin] + 1
                        else:
                            dp[v] = min(dp[v], dp[v - coin] + 1)
                else:
                    break
        return dp[amount]


if __name__ == "__main__":
    a = Solution2()
    print(a.coinChange([2], 1))