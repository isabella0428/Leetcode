class Solution1155 {
    public int numRollsToTarget(int d, int f, int target) {
        if (d == 0 || f <= 0)
            return 0;

        int[][] dp = new int[d + 1][target + 1];
        for (int i = 1; i <= f && i <= target; ++i) {
            dp[1][i] = 1;
        }

        for (int i = 2; i <= d; ++i) {
            for (int j = i; j <= i * f && j <= target; ++j) {
                for (int k = 1; k <= f; ++k) {
                    if (j - k <= 0) {
                        break;
                    }
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - k]) % (1000000007);
                }
            }
        }
        return dp[d][target];
    }
}