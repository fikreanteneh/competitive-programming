class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for i in matrix: 
            i.insert(0, float("inf"))
            i.append(float("inf"))
        n = len(matrix)
        for i in range(1, n):
            for j in range(1, n + 1):
                matrix[i][j] += min(matrix[i - 1][j], matrix[i - 1][j - 1], matrix[i - 1][j + 1])
        
        return min(matrix[-1])