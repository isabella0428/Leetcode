class Solution304 {
    int dp[][];
    int row, col;

    public static void main(String ... args) {
        Solution304 s = new Solution304();
        int [][]matrix = {
            {3, 0, 1, 4, 2}, 
            {5, 6, 3, 2, 1}, 
            {1, 2, 0, 1, 5},
            {4, 1, 0, 1, 7}, 
            {1, 0, 3, 0, 5}
        };
        s.NumMatrix(matrix);
        System.out.println(s.sumRegion(2, 1, 4, 3));
    }

    public void NumMatrix(int[][] matrix) {
        row = matrix.length;
        col = matrix[0].length;
        dp = new int[row][col];
        // Calculate sum
        // initializes the column
        int sum = 0;
        for(int i = row - 1; i >= 0; --i) {
            sum += matrix[i][col - 1];
            dp[i][col - 1] = sum;
        }

        sum = 0;
        for(int j = col - 1; j >= 0; --j) {
            sum += matrix[row - 1][j];
            dp[row - 1][j] = sum;
        }

        for(int i = row - 2; i >= 0; --i) {
            for(int j = col - 2; j >= 0; --j) {
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1] - dp[i + 1][j + 1] + matrix[i][j];
            }
        }
    }

    public int sumRegion(int row1, int col1, int row2, int col2) {
        row1 +=  1;
        col1 += 1;
        col2 += 1;
        row2 += 1;
        return dp[row1 - 1][col1 - 1]
                    - ((row2  == row) ? 0 : dp[row2][col1 - 1])
                    - ((col2 == col) ? 0 : dp[row1 - 1][col2])
                    + ((row2 == row || col2 == col) ? 0 : dp[row2][col2]);
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such: NumMatrix obj
 * = new NumMatrix(matrix); int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */