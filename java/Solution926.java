import java.util.HashMap;

class Solution926 {
    public static int minFlipsMonoIncr(String S) {
        int one_num = 0;
        int ones[] = new int[S.length()];
        for (int i= 0; i < S.length(); ++i){
            if(S.charAt(i) == '1')
                one_num += 1;
            ones[i] = one_num;
        }

        int dp[] = new int[S.length()];
        dp[0] = 0;
        for(int i = 1; i < S.length(); ++i) {
            dp[i] = Math.min(dp[i - 1], ones[i - 1]);
        }
        return dp[i];
    }

    public static void main(String ...args) {
        System.out.println(minFlipsMonoIncr("00011000"));
    }
}