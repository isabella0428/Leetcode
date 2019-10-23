class Solution:
    def minDistance(self, word1: 'str', word2: 'str') -> 'int':
        # dp[i][j]: min steps to change first i letters in word1 to first j letters in word2
        m, n = len(word1), len(word2)
        dp = [[0 for j in range(1 + n)] for i in range(1 + m)]
        for i in range(1 + m):
            dp[i][0] = i
        for j in range(1 + n):
            dp[0][j] = j
        for i in range(1, 1 + m):
            for j in range(1, 1 + n):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # dp[i][j - 1]: insertion  dp[i - 1][j]: deletion   dp[i - 1][j - 1]: replace
                    dp[i][j] = min(dp[i][j - 1], min(dp[i - 1][j], dp[i - 1][j - 1])) + 1
        return dp[m][n]


if __name__ == "__main__":
    a = Solution()
    print(a.minDistance("horse", 'ros'))

