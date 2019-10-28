import java.util.*;

class Solution1222 {
    public static List<List<Integer>> queensAttacktheKing(int[][] queens, int[] king) {
        Set<List<Integer>> result = new HashSet<>();
        Set<Integer> blocked_rows = new HashSet<>();
        Set<Integer> blocked_cols = new HashSet<>();
        // first:horizontal(0 : left, 1 : right) second:vertical (0 : top, 1 : down)
        int[][] diagnose = new int[2][2];
        int l = 0;
        int h = 0;

        queens = BubbleSort(queens, king);

        for (int i = 0; i < queens.length; ++i) {
            if (blocked_rows.contains(queens[i][0]))
                continue;
            if (blocked_cols.contains(queens[i][1]))
                continue;

            if (abs(queens[i][0] - king[0]) == abs(queens[i][1] - king[1]))
                if ((queens[i][0] - king[0] > 0 && l == 0) || (queens[i][0] - kings[0] < 0 || l != 0))
                    if ((queens[i][1] - king[1] > 0 && h == 1) || (queens[i][1] - kings[1] < 0 || h == 0)) {
                        result.push(queens[i]);
                        blocked_cols.add(queens[i][1]);
                        blocked_rows.add(queens[i][0]);
                        continue;
                    }

            if (queens[i][0] == king[0]) {
                result.push(queens[i]);
                blocked_cols.add(queens[i][1]);
                blocked_rows.add(queens[i][0]);
                continue;
            }

            if (queens[i][1] == king[1]) {
                result.push(queens[i]);
                blocked_cols.add(queens[i][1]);
                blocked_rows.add(queens[i][0]);
            }
            return result;
        }
    }

    public static int[][] BubbleSort(int[][] queens, int[] king) {
        int[] temp = new int[2];
        for (int i = 0; i < queens.length; ++i) {
            for (int j = 0; j < queens.length - i - 1; ++j) {
                if (abs(queens[i][0] - king[0]) > abs(queens[i + 1][0] - king[0])
                        || (abs(queens[i][0] - king[0]) == abs(queens[i + 1][0] - king[0])
                                && abs(queens[i][1] - king[1]) > abs(queens[i + 1][1] - king[1]))) {
                    temp = queens[i];
                    queens[i] = queens[i + 1];
                    queens[i + 1] = temp;
                }
            }
        }
        return queens;
    }
}