import copy


class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        row = len(grid)
        col = len(grid[0])
        val = copy.deepcopy(grid)
        for i in range(row):
            for j in range(col):
                val[i][j] = float('inf')
        val[0][0] = grid[0][0]

        for i in range(row):
            for j in range(col):
                if i == j == 0:
                    continue
                if j - 1 < 0:
                    val[i][j] = val[i - 1][j] + grid[i][j]
                    continue
                if i - 1 < 0:
                    val[i][j] = val[i][j - 1] + grid[i][j]
                    continue
                val[i][j] = min(val[i][j - 1], val[i - 1][j]) + grid[i][j]
        return val[row - 1][col - 1]


if __name__ == "__main__":
    a = Solution()
    print(a.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))




