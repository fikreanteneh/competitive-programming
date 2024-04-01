class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n, m = len(matrix), len(matrix[0])
        for row in matrix:
            row.append(0)
        matrix.append([0]*(m+1))
        for i in range(n):
            for j in range(m):
                matrix[i][j] += matrix[i-1][j] + matrix[i][j - 1] - matrix[i-1][j-1]
        
        answer = 0
        for topRow in range(n):
            for bottomRow in range(topRow, n):
                visited = {0:1}
                for col in range(m):
                    rowSum = matrix[bottomRow][col] - matrix[topRow - 1][col]
                    answer += visited.get(rowSum - target,  0)
                    visited[rowSum] = visited.get(rowSum, 0) + 1
        return answer
                    
                
                