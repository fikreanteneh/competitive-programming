class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        column = set()
        row = set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row.add(i)
                    column.add(j)
        for i in row:
            for j in range(m):
                matrix[i][j] = 0
        for i in column:
            for j in range(n):
                matrix[j][i] = 0