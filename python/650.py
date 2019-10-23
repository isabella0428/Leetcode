import math
class Solution:
    def minSteps(self, n: 'int') -> 'int':
        if n < 2:
            return 0
        # prime factorization
        dp = [0 for i in range(1 + n)]
        for i in range(2, 1 + n):
            dp[i] = i
            for j in range(2, int(math.sqrt(i)) + 1):
                if not i % j:
                    dp[i] = dp[j] + dp[int(i / j)]
        return dp[n]


if __name__ == "__main__":
    a = Solution()
    print(a.minSteps(3))