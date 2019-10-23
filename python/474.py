class Solution:
    def findMaxForm(self, strs: 'List[str]', m: 'int', n: 'int') -> 'int':
        # dp[i][j]  i: zeros j: ones
        dp = [[0 for j in range(1 + n)] for i in range(1 + m)]
        for string in strs:
            zeros, ones = 0, 0
            for ch in string:
                if ch == '0':
                    zeros += 1
                else:
                    ones += 1
            if m < zeros or n < ones:
                continue
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
        return dp[m][n]


if __name__ == "__main__":
    a = Solution()
    print(a.findMaxForm(["10","0001","111001","1","0"], 5, 3))