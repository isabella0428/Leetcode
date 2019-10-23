import java.util.Arrays;

class Solution1024 {
    public static void main(String ... args) {
        int [][] clips = new int[2][2];
        clips[0][0] = 0;
        clips[0][1] = 5;
        clips[1][0] = 6;
        clips[1][1] = 8;
        // clips[2][0] = 16;
        // clips[2][1] = 21;
        // clips[3][0] = 3;
        // clips[3][1] = 3;
        // clips[4][0] = 19;
        // clips[4][1] = 23;
        // clips[5][0] = 1;
        // clips[5][1] = 5;
        // clips[6][0] = 0;
        // clips[6][1] = 2;
        // clips[7][0] = 9;
        // clips[7][1] = 20;
        // clips[8][0] = 5;
        // clips[8][1] = 17;
        // clips[9][0] = 8;
        // clips[9][1] = 10;
        System.out.println(videoStitching(clips, 7));        
    }

    static public int videoStitching(int[][] clips, int T) {
        int dp[] = new int[T + 1];
        dp[0] = 7;

        for (int i = 0; i <= T; ++i) {
            dp[i] = clips.length + 1;
        }

        // bubblesort clips
        clips = bubbleSort(clips);
        for(int i = 0; i < clips.length; ++i) {
            System.out.println(String.format("%d %d", clips[i][0], clips[i][1]));
        }

        for (int i = 0; i < clips.length; ++i) {
            for (int j = clips[i][0]; j <= clips[i][1] && j <= T; ++j){
                int prev_num = clips[i][0] == 0 ? 0 : dp[clips[i][0]];
                System.out.println(dp[5]);
                dp[j] = Math.min(prev_num + 1, dp[j]);
                System.out.println(String.format("clip[%d][0], clip[%d][1], prev_num: %d, dp[clips[%d][0] - 1] : %d", i, i, prev_num, i, clips[i][0] == 0 ? 0 : dp[clips[i][0] - 1]));
            }
            if (clips[i][1] >= T)
                return dp[T] > clips.length ? -1 : dp[T];
        }
        return dp[T] > clips.length ? -1 : dp[T];
    }

    static private int[][] bubbleSort(int[][] clips) {
        for (int i = 0; i < clips.length; ++i) {
            for (int j = 0; j < clips.length - i - 1; ++j) {
                if (clips[j][0] > clips[j + 1][0] 
                || (clips[j][0] == clips[j + 1][0] 
                && clips[j][1] > clips[j + 1][1])) {
                    int[] temp = clips[j];
                    clips[j] = clips[j + 1];
                    clips[j + 1] = temp;
                }
            }
        }
        return clips;
    }
}