class Solution:
    island = 0

    def numIslands(self, grid: 'List[List[str]]') -> 'int':
        def findIsland(i, j, grid):
            grid[i][j] = '0'
            loc = [[- 1, 0], [1, 0], [0, 1], [0, -1]]
            for row_, col_ in loc:
                if -1 < i + row_ < len(grid) and -1 < j + col_ < len(grid[0]) and grid[i + row_][j + col_] == '1':
                    findIsland(i + row_, j + col_, grid)

        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    findIsland(i, j, grid)
                    self.island += 1
        return self.island


if __name__ == "__main__":
    a = Solution()
    print(a.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))