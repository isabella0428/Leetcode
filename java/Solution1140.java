import java.util.*;

class Solution1140 {
    public static int stoneGameII(int[] piles) {
       for(int n = piles.length - 2; n >= 0; --n)
            piles[n] += piles[n + 1];
        if (piles.length <= 2) return piles[0];
        int l = piles.length;
        int dp[][] = new int[l][(l + 1) / 2 + 1];

        for(int i = l - 1; i >= 0; --i) {
            int m = (l - i + 1) / 2;
            dp[i][m] = piles[i];
            while(--m > 0) {
                for(int x = 1; x <= 2 * m && i + x < l; ++x){
                    int mx = Math.min(Math.max(m, x), (l - i - x + 1) / 2);
                    dp[i][m] = Math.max(dp[i][m], piles[i] - dp[i + x][mx]);
                }
            }
        }
        return dp[0][1];
    }
}