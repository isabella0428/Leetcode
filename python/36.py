class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        length = len(board[0])
        row_dict = [{} for i in range(length)]
        col_dict = [{} for i in range(length)]
        box_dict = [{} for i in range(length)]
        for i in range(length):
            for j in range(length):
                box_index = int(i / 3) * 3 + int(j / 3)
                if board[i][j] == '.':
                    continue
                if row_dict[i].get(board[i][j], -1) != -1:
                    return False
                if col_dict[j].get(board[i][j], -1) != -1:
                    return False
                if box_dict[box_index].get(board[i][j], -1) != -1:
                    return False
                row_dict[i][board[i][j]] = board[i][j]
                col_dict[j][board[i][j]] = board[i][j]
                box_dict[box_index][board[i][j]] = board[i][j]

        return True


if __name__ == "__main__":
    a = Solution()
    print(a.isValidSudoku([["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
