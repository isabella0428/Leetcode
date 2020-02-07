// import java.util.*;

// class Solution542 {
//     BFS
//     public int[][] updateMatrix(int[][] matrix) {
//         Deque<List<Integer>> cells = new LinkedList<>();
//         int[][] dist = new int[matrix.length][matrix[0].length];
//         int row = matrix.length, col = matrix[0].length;

//         int steps = 0;
//         for (int i = 0; i < row; ++i) {
//             for (int j = 0; j < col; ++j) {
//                 if (matrix[i][j] == 0) {
//                     List<Integer> l = Arrays.asList(i, j);
//                     cells.add(l);
//                 }
//                 else {
//                     dist[i][j] = Integer.MAX_VALUE;
//                 }
//             }
//         }

//         steps++;
//         while (!cells.isEmpty()) {
//             Deque<List<Integer>> temp = new LinkedList<>();
//             while (cells.size() != 0) {
//                 List<Integer> l = cells.pop();
//                 int r = l.get(0), c = l.get(1);

//                 // Test if its up, down, left, right neighbour have been visited
//                 if (testVisited(r + 1, c, row, col, dist)) {
//                     dist[r + 1][c] = steps;
//                     temp.add(Arrays.asList(r + 1, c));
//                 }

//                 if (testVisited(r - 1, c, row, col, dist)) {
//                     dist[r - 1][c] = steps;
//                     temp.add(Arrays.asList(r - 1, c));
//                 }

//                 if (testVisited(r, c + 1, row, col, dist)) {
//                     dist[r][c + 1] = steps;
//                     temp.add(Arrays.asList(r, c + 1));
//                 }

//                 if (testVisited(r, c - 1, row, col, dist)) {
//                     dist[r][c - 1] = steps;
//                     temp.add(Arrays.asList(r, c - 1));
//                 }
//             }
//             cells = temp;
//             steps++;
//         }
//         return dist;
//     }

//     private boolean testVisited(int i, int j, int row, int col, int[][] dist) {
//         if (i < 0 || i >= row || j < 0 || j >= col || dist[i][j] != Integer.MAX_VALUE)
//             return false;
//         return true;
//     }
// }

class Solution542 {
    // DP
    public int[][] updateMatrix(int[][] matrix) {
        int row = matrix.length, col = matrix[0].length;
        int[][] dp = new int[row][col];
        for (int i = 0; i < row; ++i) {
            for (int j = 0; j < col; ++j) {
                dp[i][j] = Integer.MAX_VALUE - 100000;
            }
        }

        for (int i = 0; i < row; ++i) {
            for (int j = 0; j < col; ++j) {
                if (matrix[i][j] == 0) {
                    dp[i][j] = 0;
                } else {
                    if (i > 0)
                        dp[i][j] = Math.min(dp[i][j], dp[i - 1][j] + 1);
                    if (j > 0)
                        dp[i][j] = Math.min(dp[i][j], dp[i][j - 1] + 1);
                }
            }
        }

        for (int i = row - 1; i >= 0; --i) {
            for (int j = col - 1; j >= 0; --j) {
                if (i < row - 1)
                    dp[i][j] = Math.min(dp[i][j], dp[i + 1][j] + 1);
                if (j < col - 1)
                    dp[i][j] = Math.min(dp[i][j], dp[i][j + 1] + 1);
            }
        }
        return dp;
    }
}