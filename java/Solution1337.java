import java.util.*;

class Solution1337 {
    public int[] kWeakestRows(int[][] mat, int k) {
        PriorityQueue<int[]> maxQ = new PriorityQueue<>((a, b) -> a[0] != b[0] ? b[0] - a[0] : b[1] - a[1]);

        for (int i = 0; i < mat.length; ++i) {
            int num = 0;
            for(int j = 0; j < mat[i].length; ++j) {
                if (mat[i][j] == 1) {
                    ++num;
                } else {
                    break;
                }
            }
            
            maxQ.offer(new int[]{num, i});
            if (maxQ.size() > k) {
                maxQ.poll();
            }
        }

        int ret[] = new int[k];
        while (k > 0)
            ret[--k] = maxQ.poll()[1];
        return ret;
    }
}