class Solution1:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        spatial = [matrix[0][0]]
        length = len(matrix[0]) - 1
        width = len(matrix) - 1
        dict = {'right': (length, [0, 1]), 'left': (length, [0, -1]), 'down': (width, [1, 0]),
                'up': (width, [-1, 0])}
        row, col = 0, 0
        while 1:
            if len(spatial) >= len(matrix) * len(matrix[0]):
                return spatial
            for dir in ["right", "down", "left", "up"]:
                length, step = dict[dir]
                for i in range(length):
                    if matrix[row + step[0]][col + step[1]] in spatial:
                        break
                    row += step[0]
                    col += step[1]
                    spatial.append(matrix[row][col])
                    if len(spatial) >= len(matrix) * len(matrix[0]):
                        return spatial
        return spatial


class Solution2:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        def isValid(matrix, row, col, m, n):
            if row < 0 or row > m - 1 or col < 0 or col > n - 1:
                return False
            if matrix[row][col] == '@':
                return False
            return True

        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        row, col = 0, 0
        ret = []
        index = 0
        step = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while len(ret) != m * n:
            if matrix[row][col] != '@':
                ret.append(matrix[row][col])
                matrix[row][col] = '@'
            delta = step[index]
            if not isValid(matrix, row + delta[0], col + delta[1], m, n):
                index = (index + 1) % 4
            delta = step[index]
            row += delta[0]
            col += delta[1]
        return ret


if __name__ == "__main__":
    a = Solution2()
    print(a.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))