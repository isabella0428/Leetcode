import java.util.*;

class Solution120 {
    public int minimumTotal(List<List<Integer>> triangle) {
        int row = triangle.size();
        int dp[] = new int[triangle.get(row - 1).size()];
        
        for(int j = 0; j < triangle.get(row - 1).size(); ++j) {
            dp[j] = triangle.get(row - 1).get(j);
        }
        
        for(int i = row - 2; i >= 0; --i) {
            for(int j = 0; j <= i; ++j) {
                dp[j] = Math.min(dp[j],dp[j + 1]) + triangle.get(i).get(j);
            }
        }
        return dp[0];
    }
}