class Solution1223 {
    /*
    Problem:    1223. Dice Roll Simulation
    A die simulator generates a random number from 1 to 6 for each roll. 
    You introduced a constraint to the generator such that it cannot roll
    the number i more than rollMax[i] (1-indexed) consecutive times. 

    Given an array of integers rollMax and an integer n, return the number 
    of distinct sequences that can be obtained with exact n rolls.
    Two sequences are considered different if at least one element differs 
    from each other. Since the answer may be too large, return it modulo 10^9 + 7.
    */

    public static int dieSimulator(int n, int[] rollMax) {
        int num_sequence = 0;
        int[][][] dp = new int[n][6][16];

        for (int i = 0; i < 6; ++i) {
            dp[0][i][1] = 1;
        }

        for (int i = 1; i < n; ++i) {
            for (int j = 0; j < 6; ++j) { // nth digit
                for (int p = 0; p < 6; ++p) { // (n - 1)th digit
                    for (int k = 0; k <= rollMax[p]; ++k)
                        if (p != j) {
                            dp[i][j][1] = (dp[i - 1][p][k] + dp[i][j][1]) % 1000000007;
                        } else {
                            if (k != rollMax[p])
                                dp[i][j][k + 1] = (dp[i][j][k + 1] + dp[i - 1][j][k]) % 1000000007;
                        }
                }
            }
        }
        for (int i = 0; i < 6; ++i) {
            for (int j = 0; j <= 15; ++j) {
                num_sequence = (num_sequence + dp[n - 1][i][j]) % 1000000007;
            }
        }
        return num_sequence % 1000000007;
    }

    public static void main(String ... args) {
        int [] max_num = {7, 5, 15, 5, 1, 7};
        System.out.println(dieSimulator(100, max_num));
    }
}