class Solution:

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        def search(matrix, target, row_range, col_range):
            if row_range[0] > row_range[1] or col_range[0] > col_range[1]:
                return False
            row = int(sum(row_range) / 2)
            col = int(sum(col_range) / 2)
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                return search(matrix, target, [row_range[0], row - 1], col_range) or search(matrix, target, row_range,
                                                                                            [col_range[0], col - 1])
            else:
                return search(matrix, target, [row + 1, row_range[1]], col_range) or search(matrix, target, row_range,
                                                                                            [col + 1, col_range[1]])
            return False

        if not matrix:
            return False
        return search(matrix, target, [0, len(matrix) - 1], [0, len(matrix[0]) - 1])


if __name__ == "__main__":
    a = Solution()
    print(a.searchMatrix([[1, 3,  5,  7],[10, 11, 16, 20],[23, 30, 34, 50]], 3))