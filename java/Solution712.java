import java.util.*;

class Solution712 {
    /***
        Problem discription:    
        Delete characters in two Strings to make the strings match
        Return the smallest ASCII sum

        Solution:
        Apply bottom up dynamic programming
    */
    public int minimumDeleteSum(String s1, String s2) {
        int l1 = s1.length();
        int l2 = s2.length();
        int dp[][] = new int [l1 + 1][l2 + 1];
        
        for (int i = 0; i <= l1; ++i) {
            for (int j = 0; j <= l2; ++j) {
                dp[i][j] = Integer.MAX_VALUE;
            }
        }
        
        dp[l1][l2] = 0;
        for (int i = l1 - 1; i >= 0; --i) {
            dp[i][l2] = dp[i + 1][l2] + s1.charAt(i);
        }
        
        for (int j = l2 - 1; j >= 0; --j) {
            dp[l1][j] = dp[l1][j + 1] + s2.charAt(j);
        }
        
        for (int i = l1 - 1; i >= 0; --i) {
            for (int j = l2 - 1; j >= 0; --j) {
                if (j == l2 || i == l1)
                    continue;
                if (s1.charAt(i) == s2.charAt(j)) {
                    dp[i][j] = dp[i + 1][j +1];
                }    
                else {
                    //delete s1
                    dp[i][j] = Math.min(dp[i + 1][j] + s1.charAt(i), dp[i][j]);
                    //delete s2
                    dp[i][j] = Math.min(dp[i][j + 1] + s2.charAt(j), dp[i][j]);
                    //All delete
                    dp[i][j] = Math.min(dp[i + 1][j + 1] + s1.charAt(i) + s2.charAt(j), dp[i][j]);
                }
            }
        }
        return dp[0][0];
    }
}