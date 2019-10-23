class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def search(board, word, i, j):
            if word[0] != board[i][j]:
                return False
            if not word[1:]:
                return True
            val, board[i][j] = board[i][j], '@'
            if i > 0 and search(board, word[1:], i - 1, j):
                return True
            if i < len(board) - 1 and search(board, word[1:], i + 1, j):
                return True
            if j > 0 and search(board, word[1:], i, j - 1):
                return True
            if j < len(board[0]) - 1 and search(board, word[1:], i, j + 1):
                return True
            board[i][j] = val
            return False

        if not word:
            return True
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if search(board, word, i, j):
                    return True
        return False


if __name__ == "__main__":
    a = Solution()
    print(a.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
,"ABCCED"))







