import copy
class Solution:
    def pacificAtlantic(self, matrix: 'List[List[int]]') -> 'List[List[int]]':
        def dfs(i, j, visited, matrix, m, n):
            direction = [[1, 0], [-1, 0], [0, -1], [0, 1]]
            visited[i][j] = True
            for dir in direction:
                x, y = i + dir[0], j + dir[1]
                if x < 0 or x > m - 1 or y < 0 or y > n - 1 or matrix[x][y] < matrix[i][j] or visited[x][y]:
                    continue
                dfs(x, y, visited, matrix, m, n)

        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        p_visited = [[False for a in range(n)] for b in range(m)]
        a_visited = copy.deepcopy(p_visited)
        for i in range(m):
            # flow to Pacific Ocean
            dfs(i, 0, p_visited, matrix, m, n)
            dfs(i, n - 1, a_visited, matrix, m, n)

        for j in range(n):
            # flow to Atlantic Ocean
            dfs(0, j, p_visited, matrix, m, n)
            dfs(m - 1, j, a_visited, matrix, m, n)

        loc = []
        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    loc.append([i, j])
        return loc


if __name__ == "__main__":
    a = Solution()
    print(a.pacificAtlantic([[1, 2, 2, 3, 5],[3, 2, 3, 4, 4],[2, 4, 5, 3,1],[6,7,1,4,5],[5,1,1,2,4]]))