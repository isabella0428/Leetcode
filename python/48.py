class Solution:
    def rotate(self, matrix):

        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        length = len(matrix)
        for i in range(length):
            for j in range(i):
                if i == j:
                    continue
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


if __name__ == "__main__":
    a = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    a.rotate(matrix)
    print(matrix)