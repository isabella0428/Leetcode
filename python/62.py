class Solution:
    def __init__(self):
        self.memo = []

    def uniquePaths(self, m, n):        #dynamic programming bottom-up
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        tmp = [0 for i in range(n + 1)]
        self.memo = [tmp[:] for i in range(m + 1)]
        row, col = 1, 1
        self.memo[row][col] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1 and j == 1:
                    continue
                self.memo[i][j] = self.memo[i - 1][j] + self.memo[i][j - 1]

        return self.memo[m][n]


if __name__ == "__main__":
    a = Solution()
    print(a.uniquePaths(7, 3))


