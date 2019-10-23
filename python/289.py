class Solution:
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """

        def check(board, i, j):
            count = 0
            for delta_x in range(-1, 2):
                for delta_y in range(-1, 2):
                    if 0 <= i + delta_x <= len(board) - 1 and 0 <= j + delta_y <= len(board[0]) - 1 and not (
                            delta_x == delta_y == 0) and board[i + delta_x][j + delta_y] == 1:
                        count += 1
            return count

        live = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]:
                    if 2 <= check(board, i, j) <= 3:
                        live.append([i, j])
                else:
                    if check(board, i, j) == 3:
                        live.append([i, j])
        for i in range(len(board)):
            for j in range(len(board[0])):
                if [i, j] in live:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
        return board


if __name__ == "__main__":
    a = Solution()
    print(a.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))



    