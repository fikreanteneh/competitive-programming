class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n, m = len(matrix), len(matrix[0])
        check = {}
        for i in range(m):
            check[0 - i] = matrix[0][i]
        for i in range(n):
            check[i - 0] = matrix[i][0]
        for i in range(m * n):
            row = i // m
            col = i % m
            if check[row - col] != matrix[row][col]:
                return False
        return True