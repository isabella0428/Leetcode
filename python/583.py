class Solution:
    def minDistance(self, word1: 'str', word2: 'str') -> 'int':
        word1, word2 = list(word1), list(word2)
        m, n = len(word1), len(word2)
        # dp[i][j]: word1[:i] and word2[:j] have in common
        dp = [[0 for j in range(1 + n)] for i in range(1 + m)]
        for i in range(1, 1 + m):
            for j in range(1, 1 + n):
                if word2[j - 1] == word1[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return m + n - 2 * dp[m][n]


if __name__ == "__main__":
    a = Solution()
    print(a.minDistance(
"intention",
"execution"))


