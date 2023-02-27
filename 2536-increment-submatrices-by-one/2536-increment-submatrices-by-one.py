class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matrix = [[0] *( n + 1) for j in range(n)]
        
        for query in queries:
            for i in range(query[0], query[2] + 1):
                matrix[i][query[1]] += 1
                matrix[i][query[3] + 1] -= 1
        for column in matrix:
            sums = 0
            for i in range(n):
                sums += column[i]
                column[i] = sums
            column.pop()
                
        return matrix
        
        
        # 1 0 -1 0   1 1 0 0
        # 1 1 -1 -1  1 2 1 0
        # 0 1 0 -1   0 1 1 0
        
        