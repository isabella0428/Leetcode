class Solution:
    def maxAreaOfIsland(self, grid: 'List[List[int]]') -> 'int':
        def search(row, col, grid, num):
            grid[row][col] = 0
            up = 0 if row == 0 else grid[row - 1][col]
            if up:
                num += search(row - 1, col, grid, 1)
            down = 0 if row == m - 1 else grid[row + 1][col]
            if down:
                num += search(row + 1, col, grid, 1)
            left = 0 if col == 0 else grid[row][col - 1]
            if left:
                num += search(row, col - 1, grid, 1)
            right = 0 if col == n - 1 else grid[row][col + 1]
            if right:
                num += search(row, col + 1, grid, 1)
            return num

        m, n = len(grid), len(grid[0])
        index = [[i,j] for i in range(m) for j in range(n) if grid[i][j] == 1]
        max_term = 0
        for loc in index:
            row, col = loc[0], loc[1]
            grid[row][col] = 0
            max_term = max(max_term, search(row, col, grid[:], 1))
            grid[row][col] = 1

        return max_term


if __name__ == "__main__":
    a = Solution()
    print(a.maxAreaOfIsland(
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]))
