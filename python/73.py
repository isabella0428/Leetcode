class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        stack = []
        n = len(matrix[0])             #col
        m = len(matrix)          #row
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    stack.append([i, j])
        for item in stack:
            matrix[item[0]] = [0 for i in range(n)]
            for i in range(m):
                matrix[i][item[1]] = 0


if __name__ == "__main__":
    a = Solution()
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    a.setZeroes(matrix)
    print(matrix)



