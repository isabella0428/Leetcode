class Solution1219 {
    int gold_sum = 0;

    public int getMaximumGold(int[][] grid) {
        int row = grid.length;
        int col = grid[0].length;

        for (int i = 0; i < row; ++i) {
            for (int j = 0; j < col; ++j) {
                if (grid[i][j] == 0)
                    continue;
                int temp = grid[i][j];
                grid[i][j] = 0;
                DFS(i, j, grid, temp);
                grid[i][j] = temp;
            }
        }
        return gold_sum;
    }

    public void DFS(int i, int j, int[][] grid, int gold) {
        if ((check(i + 1, j, grid) == 0) && (check(i - 1, j, grid) == 0) && (check(i, j + 1, grid) == 0)
                && (check(i, j - 1, grid) == 0)) {
            gold_sum = Math.max(gold_sum, gold);
            return;
        }

        if (check(i + 1, j, grid) == 1) {
            int temp = grid[i + 1][j];
            grid[i + 1][j] = 0;
            DFS(i + 1, j, grid, gold + temp);
            grid[i + 1][j] = temp;
        }

        if (check(i - 1, j, grid) == 1) {
            int temp = grid[i - 1][j];
            grid[i - 1][j] = 0;
            DFS(i - 1, j, grid, gold + temp);
            grid[i - 1][j] = temp;
        }

        if (check(i, j + 1, grid) == 1) {
            int temp = grid[i][j + 1];
            grid[i][j + 1] = 0;
            DFS(i, j + 1, grid, gold + temp);
            grid[i][j + 1] = temp;
        }

        if (check(i, j - 1, grid) == 1) {
            int temp = grid[i][j - 1];
            grid[i][j - 1] = 0;
            DFS(i, j - 1, grid, gold + temp);
            grid[i][j - 1] = temp;
        }
        return;
    }

    public int check(int i, int j, int[][] grid) {
        if (i >= grid.length || i < 0)
            return 0;
        if (j >= grid[0].length || j < 0)
            return 0;
        if (grid[i][j] == 0)
            return 0;
        return 1;
    }
}