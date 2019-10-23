import copy


class Solution1:
    def __init__(self):
        self.ret = []

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        def checkDiagnoal(row1, col1, n, tmp):
            Flag = True
            row, col = row1, col1
            while n - 1 >= row >= 0 and col >= 0:
                if tmp[row][col] == 'Q':
                    Flag = False
                    break
                col -= 1
                row += 1
            row, col = row1, col1
            while n - 1 >= row >= 0 and col >= 0:
                if tmp[row][col] == 'Q':
                    Flag = False
                    break
                col -= 1
                row -= 1
            return Flag

        def Queens(n, count, tmp):
            if count == n:              # count: col filled
                self.ret.append(copy.deepcopy(tmp))
                return

            for i in range(n):          # i: row_num
                if 'Q' in tmp[i]:       # row: no same values
                    continue
                row, col = i, count
                Flag = checkDiagnoal(row, col, n, tmp)   #check diagonals
                if not Flag:
                    continue
                tmp[i] = tmp[i][:count] + 'Q' + tmp[i][count + 1:]
                tmp_new = copy.deepcopy(tmp)
                Queens(n, count + 1, tmp_new)
                tmp[i] = tmp[i][:count] + '.' + tmp[i][count + 1:]

        default = "." * n
        default = [default for i in range(n)]
        for row_num in range(n):
            tmp = copy.deepcopy(default)
            tmp[row_num] = 'Q' + tmp[row_num][1:]
            Queens(n, 1, tmp)
        return self.ret


class Solution2:
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
        return [['.' * i + "Q" + '.' * (n - i - 1) for i in sol] for sol in result]


class Solution3:
    cnt = 0

    def solveNQueens(self, n: int):
        def _better_print(matrix):
            """
            Visualizes the output
            :param matrix: List[int]    stores the locations of queens in diffferent rows
            :return: None
            """
            for num in matrix:
                s = []
                for i in range(n):
                    if i == num:
                        s.append('Q')
                    else:
                        s.append('.')
                print("\t".join(s))

        def _checkDiagonal(matrix, cur, target):
            """
            Checks if target meets diagonal requirements
            :param matrix: List[int]    stores locations of queens in different rows
            :param cur: int             current row
            :param target: int          column to be evaluated
            :return: boolean            whether target meets the constraint of diagonal
            """
            for i in range(1, cur + 1):
                if matrix[cur - i] == target - i or matrix[cur - i] == target + i:
                    return False
            return True

        def _DFS(matrix, cur):
            """
            Uses depth-first search to find all results
            :param matrix: List[int]    stores locations of queens in different rows
            :param cur: int             current row
            :return: None
            """
            if cur == n:
                ret.append(matrix)
                return
            for i in range(n):
                if i not in matrix:
                    if _checkDiagonal(matrix, cur, i):
                        matrix[cur] = i
                        _DFS(matrix[:], cur + 1)
                        matrix[cur] = -1

        def _format(ret):
            """
            Formats the result into the desired form
            :param ret: List[List[str]]     stores the output in desired forms
            :return: None
            """
            for item in ret:
                tmp = []
                for num in item:
                    s = []
                    for i in range(n):
                        if i == num:
                            s.append('Q')
                        else:
                            s.append('.')
                    tmp.append("".join(s))
                out.append(tmp)

        matrix = [-1 for i in range(n)]
        ret, out = [], []
        _DFS(matrix[:], 0)
        format(ret)
        return out


if __name__ == "__main__":
    a = Solution3()
    print(a.solveNQueens(5))