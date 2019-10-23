class Solution:
    def solveNQueens(self, n):
        def DFS(queens, xy_diff, xy_sum):
            p = len(queens)
            if p == n:                  #row
                result.append(queens)
                return
            for q in range(n):          #col
                if q not in queens and p - q not in xy_diff and p + q not in xy_sum:
                    DFS(queens + [q], xy_diff + [p - q], xy_sum + [p + q])
        result = []
        DFS([], [], [])
        return len(result)


if __name__ == "__main__":
    a = Solution()
    print(a.solveNQueens(4))