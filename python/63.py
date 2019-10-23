class Solution1:
    # dynamic programming
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid[0]), len(obstacleGrid)      #col, row
        obstacleGrid.insert(0, [0 for i in range(m + 1)])
        for i in range(1, n + 1):
            obstacleGrid[i].insert(0, 0)      #correspond with the actual size
        tmp = [0 for i in range(m + 1)]
        Path = [tmp[:] for i in range(n + 1)]
        if obstacleGrid[1][1] == 0:
            Path[1][1] = 1
        else:
            return 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if i == j == 1 or obstacleGrid[i][j] == 1:
                    continue
                Path[i][j] = Path[i][j - 1] + Path[i - 1][j]
        return Path[n][m]


class Solution2:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        dp[0][0] = 1
        for i in range(1, m):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = dp[i - 1][0]
        for j in range(1, n):
            if obstacleGrid[0][j] != 1:
                dp[0][j] = dp[0][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]


if __name__ == "__main__":
    a = Solution2()
    print(a.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))


