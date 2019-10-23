from copy import deepcopy


class Solution:
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        dp = deepcopy(matrix)
        m, n = len(matrix), len(matrix[0])
        max_term = 0
        for i in range(m):
            for j in range(n):
                dp[i][j] = int(dp[i][j])
                max_term = max(max_term, dp[i][j])

        for i in range(1, m):
            for j in range(1, n):
                if dp[i][j]:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    max_term = max(max_term, dp[i][j])
        return int(max_term) ** 2


if __name__ == "__main__":
    a = Solution()
    print(a.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
