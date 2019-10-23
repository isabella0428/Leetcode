class MySolution:
    def solve(self, board: 'List[List[str]]') -> 'None':
        """
        Do not return anything, modify board in-place instead.
        """

        def dfs(i, j, tmp):
            nonlocal flag
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                flag = False
                return
            if board[i][j] != 'O' or [i, j] in tmp:
                return
            tmp.append([i, j])
            dfs(i - 1, j, tmp)
            dfs(i + 1, j, tmp)
            dfs(i, j + 1, tmp)
            dfs(i, j - 1, tmp)
            return tmp

        change = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and [i, j] not in change:
                    tmp = []
                    flag = True
                    tmp = dfs(i, j, tmp[:])
                    if flag:
                        for loc in tmp:
                            i, j = loc[0], loc[1]
                            board[i][j] = 'X'

        for loc in change:
            i, j = loc[0], loc[1]
            board[i][j] = 'X'


class Solution:
    # Phase 1: "Save" every O-region touching the border, changing its cells to 'S'.
    # Phase 2: Change every 'S' on the board to 'O' and everything else to 'X'.
    def solve(self, board: 'List[List[str]]') -> 'None':
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m, n = len(board), len(board[0])
        save = [ij for k in range(m + n) for ij in ((0, k), (m - 1, k), (k, 0), (k, n - 1))]
        while save:
            i, j = save.pop()
            if -1 < i < m and -1 < j < n and board[i][j] == 'O':
                board[i][j] = 'S'
                save += (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)
        for row in board:
            for i, c in enumerate(row):
                row[i] = 'XO'[c == 'S']


if __name__ == "__main__":
    a = Solution()
    board = [['O']]
    a.solve(board)
    print(board)
