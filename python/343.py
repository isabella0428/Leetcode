class Solution:
    def integerBreak(self, n: 'int') -> 'int':
        memo = [i - 1 for i in range(n + 1)]
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        memo[0], memo[1] = 1, 1
        for i in range(3, n + 1):
            memo[i] = max([max(memo[i - k], i - k) * max(k, memo[k]) for k in range(1, i)])
        return memo[n]


if __name__ == "__main__":
    a = Solution()
    print(a.integerBreak(3))


