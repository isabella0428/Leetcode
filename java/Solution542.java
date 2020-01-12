import java.util.*;

class Solution542 {
    public int[][] updateMatrix(int[][] matrix) {
        Deque<List<Integer>> cells = new LinkedList<>();
        int[][] visited = new int[matrix.length][matrix[0].length];
        int[][] dist = new int[matrix.length][matrix[0].length];
        int row = matrix.length, col = matrix[0].length;

        int steps = 0, visit = 0;
        for (int i = 0; i < row; ++i) {
            for (int j = 0; j < col; ++j) {
                if (matrix[i][j] == 0) {
                    List<Integer> l = Arrays.asList(i, j);
                    cells.add(l);
                    // Mark them as visited
                    visited[i][j] = 1;
                    visit++;
                }
            }
        }

        steps++;
        while (visit < row * col) {
            Deque<List<Integer>> temp = new LinkedList();
            while (cells.size() != 0) {
                List<Integer> l = cells.pop();
                int r = l.get(0), c = l.get(1);

                // Test if its up, down, left, right neighbour have been visited
                if (testVisited(r + 1, c, row, col, visited)) {
                    visited[r + 1][c] = 1;
                    dist[r + 1][c] = steps;
                    visit++;
                    temp.add(Arrays.asList(r + 1, c));
                }

                if (testVisited(r - 1, c, row, col, visited)) {
                    visited[r - 1][c] = 1;
                    dist[r - 1][c] = steps;
                    visit++;
                    temp.add(Arrays.asList(r - 1, c));
                }

                if (testVisited(r, c + 1, row, col, visited)) {
                    visited[r][c + 1] = 1;
                    dist[r][c + 1] = steps;
                    visit++;
                    temp.add(Arrays.asList(r, c + 1));
                }

                if (testVisited(r, c - 1, row, col, visited)) {
                    visited[r][c - 1] = 1;
                    dist[r][c - 1] = steps;
                    visit++;
                    temp.add(Arrays.asList(r, c - 1));
                }
            }
            cells = temp;
            steps++;
        }
        return dist;
    }

    private boolean testVisited(int i, int j, int row, int col, int visited[][]) {
        if (i < 0 || i >= row)
            return false;

        if (j < 0 || j >= col)
            return false;

        if (visited[i][j] == 1)
            return false;

        return true;
    }
}