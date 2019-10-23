import java.util.*;

class Solution {
    public int maxSumAfterPartitioning(int[] A, int K) {
         int length = A.length;
         int dp[] = new int[length];
         for(int i = 0; i < length; ++i) {
            int curMax = Integer.MIN_VALUE;
            for(int k = 1; k <= K && i - k + 1 >= 0; ++k) {
                curMax = Math.max(curMax, A[i - k + 1]);
                dp[i] = Math.max(dp[i], (i >= k ? dp[i - k]  : 0 )+ k * curMax);
            }
         }
         return dp[length - 1];
    }
}