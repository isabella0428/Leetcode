class Solution1:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        output = [None for i in range(n)]
        output = [output[:] for i in range(n)]
        count = 2
        i, j = 0, 0
        output[i][j] = 1
        if count == n * n + 1:
            return output
        while 1:
            for delta_row, delta_col in delta:
                while i + delta_row <= n - 1 and j + delta_col <= n - 1:
                    if output[i + delta_row][j + delta_col] == None:
                        i += delta_row
                        j += delta_col
                        output[i][j] = count
                        count += 1
                        if count == n * n + 1:
                            return output
                    else:
                        break


class Solution2:
    def generateMatrix(self, n: int):
        def check(ret, row, col, n):
            if row < 0 or row >= n or col < 0 or col >= n:
                return False
            if ret[row][col] != -1:
                return False
            return True

        step = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        ret, i = [[-1 for i in range(n)] for j in range(n)], 2
        row, col = 0, 0
        ret[0][0] = 1
        while 1:
            for delta in step:
                if i == n ** 2 + 1:
                    return ret
                while check(ret, row + delta[0], col + delta[1], n):
                    row += delta[0]
                    col += delta[1]
                    ret[row][col] = i
                    i += 1
        return ret


if __name__ == "__main__":
    a = Solution2()
    print(a.generateMatrix(3))
