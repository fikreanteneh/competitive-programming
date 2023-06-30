class Solution:
    def rotate(self, matrix: List[List[int]], m = 0) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) - m - 1
        if n <= 0 or m >= n:
            return
        for i in range(0, n - m):
            indexes = ( (m + i ,n), (n, n - i), (n-i, m))
            for x,y in indexes:
                matrix[m][m + i], matrix[x][y] = matrix[x][y], matrix[m][m + i]
        return self.rotate(matrix, m + 1)